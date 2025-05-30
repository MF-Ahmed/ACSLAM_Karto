/**
* Modified by jplaced, jjgomez
* 2022, University of Zaragoza
*/

#include "Node.h"

// string to store the robot namespace
std::string _robot_namespace_;

Node::Node (ORB_SLAM2::System::eSensor sensor, ros::NodeHandle &node_handle, image_transport::ImageTransport &image_transport) :
    image_transport_(image_transport),
    was_lost_(false) {
        name_of_node_ = ros::this_node::getName();
        node_handle_ = node_handle;
        min_observations_per_point_ = 2;
        sensor_ = sensor;
}


Node::~Node () {
    // Stop all threads
    orb_slam_->Shutdown();
    delete orb_slam_;
}

void Node::Init () {
    // Static ROS parameters
    initializeParams(node_handle_);

    // Create a parameters object to pass to the Tracking system
    ORB_SLAM2::ORBParameters parameters;
    LoadOrbParameters (parameters);

    orb_slam_ = new ORB_SLAM2::System (voc_file_name_param_, sensor_, parameters, map_file_name_param_, load_map_param_);

    service_server_ = node_handle_.advertiseService(name_of_node_+"/save_map", &Node::SaveMapSrv, this);

    //Setup dynamic reconfigure
    dynamic_reconfigure::Server<orb_slam2_ros::dynamic_reconfigureConfig>::CallbackType dynamic_param_callback;
    dynamic_param_callback = boost::bind(&Node::ParamsChangedCallback, this, _1, _2);
    dynamic_param_server_.setCallback(dynamic_param_callback);

    // Initialization transformation listener
    tfBuffer.reset(new tf2_ros::Buffer);
    tfListener.reset(new tf2_ros::TransformListener(*tfBuffer));

    rendered_image_publisher_ = image_transport_.advertise (name_of_node_+"/tracking_image", 1);
    if (publish_pointcloud_param_) {
        map_points_publisher_ = node_handle_.advertise<sensor_msgs::PointCloud2> (name_of_node_+"/map_points", 1);
    }

    // Enable publishing camera's pose as PoseStamped message
    if (publish_pose_param_) {
        pose_publisher_ = node_handle_.advertise<geometry_msgs::PoseStamped> (name_of_node_+"/camera_pose", 1);
    }

    // Publishing gba and tracking states
    status_gba_publisher_ = node_handle_.advertise<std_msgs::Bool> (name_of_node_+"/gba_running", 1);
    state_publisher_ = node_handle_.advertise<orb_slam2_ros::ORBState>(name_of_node_+"/info/state", 10);
    state_desc_publisher_  = node_handle_.advertise<std_msgs::String>(name_of_node_+"/info/state_description", 10);

    // Robot odometry subscriber
    odom_subscriber_ = node_handle_.subscribe<nav_msgs::Odometry>("/odom", 10, &Node::OdomCallback, this);

    // Graph publisher
    vertex_publisher_ = node_handle_.advertise<std_msgs::Float64MultiArray> (name_of_node_+"/vertex_list", 1);
    edge_publisher_ = node_handle_.advertise<std_msgs::Float64MultiArray> (name_of_node_+"/edge_list", 1);
    point_publisher_ = node_handle_.advertise<std_msgs::Float64MultiArray> (name_of_node_+"/point_list", 1);

}


void Node::initializeParams(ros::NodeHandle &nh){
    nh.param<bool>(name_of_node_+ "/publish_pointcloud", publish_pointcloud_param_, true);
    nh.param<bool>(name_of_node_+ "/publish_pose", publish_pose_param_, true);
    nh.param<bool>(name_of_node_+ "/publish_tf", publish_tf_param_, true);

    // Getting the namespace param from the launch file
    nh.getParam(name_of_node_+"/robot_namespace",_robot_namespace_);

    nh.param<std::string>(name_of_node_+ "/pointcloud_frame_id", map_frame_id_param_, _robot_namespace_+"/map");
    nh.param<std::string>(name_of_node_+ "/camera_frame_id", camera_frame_id_param_, _robot_namespace_+"/camera_link");
    nh.param<std::string>(name_of_node_+ "/target_frame_id", target_frame_id_param_, _robot_namespace_+"/base_link");
    nh.param<std::string>(name_of_node_ + "/map_file", map_file_name_param_, "map.bin");
    nh.param<std::string>(name_of_node_ + "/voc_file", voc_file_name_param_, "file_not_set");

    nh.param<bool>(name_of_node_ + "/load_map", load_map_param_, false);

}


void Node::LoadOrbParameters (ORB_SLAM2::ORBParameters& parameters) {
    //ORB SLAM configuration parameters
    node_handle_.param(name_of_node_ + "/camera_fps", parameters.maxFrames, 30);
    node_handle_.param(name_of_node_ + "/camera_rgb_encoding", parameters.RGB, true);
    node_handle_.param(name_of_node_ + "/ORBextractor/nFeatures", parameters.nFeatures, 1200);
    node_handle_.param(name_of_node_ + "/ORBextractor/scaleFactor", parameters.scaleFactor, static_cast<float>(1.2));
    node_handle_.param(name_of_node_ + "/ORBextractor/nLevels", parameters.nLevels, 8);
    node_handle_.param(name_of_node_ + "/ORBextractor/iniThFAST", parameters.iniThFAST, 20);
    node_handle_.param(name_of_node_ + "/ORBextractor/minThFAST", parameters.minThFAST, 7);

    bool load_calibration_from_cam = false;
    node_handle_.param(name_of_node_ + "/load_calibration_from_cam", load_calibration_from_cam, false);

    if (sensor_== ORB_SLAM2::System::STEREO || sensor_==ORB_SLAM2::System::RGBD) {
        node_handle_.param(name_of_node_ + "/ThDepth", parameters.thDepth, static_cast<float>(35.0));
        node_handle_.param(name_of_node_ + "/depth_map_factor", parameters.depthMapFactor, static_cast<float>(1.0));
    }

    if (load_calibration_from_cam) {
        ROS_INFO_STREAM ("Listening for camera info on topic " << node_handle_.resolveName(camera_info_topic_));
        sensor_msgs::CameraInfo::ConstPtr camera_info = ros::topic::waitForMessage<sensor_msgs::CameraInfo>(camera_info_topic_, ros::Duration(1000.0));
        if(camera_info == nullptr){
            ROS_WARN("Did not receive camera info before timeout, defaulting to launch file params.");
        } else {
            parameters.fx = camera_info->K[0];
            parameters.fy = camera_info->K[4];
            parameters.cx = camera_info->K[2];
            parameters.cy = camera_info->K[5];

            parameters.baseline = 30;

            if (sensor_== ORB_SLAM2::System::STEREO || sensor_==ORB_SLAM2::System::RGBD) {
                node_handle_.getParam(name_of_node_ + "/camera_bf", parameters.baseline);
            }

            parameters.k1 = camera_info->D[0];
            parameters.k2 = camera_info->D[1];
            parameters.p1 = camera_info->D[2];
            parameters.p2 = camera_info->D[3];
            parameters.k3 = camera_info->D[4];
            return;
        }
    }

    bool got_cam_calibration = true;
    if (sensor_== ORB_SLAM2::System::STEREO || sensor_==ORB_SLAM2::System::RGBD) {
        got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_baseline", parameters.baseline);
    }

    got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_fx", parameters.fx);
    got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_fy", parameters.fy);
    got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_cx", parameters.cx);
    got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_cy", parameters.cy);
    got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_k1", parameters.k1);
    got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_k2", parameters.k2);
    got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_p1", parameters.p1);
    got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_p2", parameters.p2);
    got_cam_calibration &= node_handle_.getParam(name_of_node_ + "/camera_k3", parameters.k3);

    if (!got_cam_calibration) {
        ROS_ERROR ("Failed to get camera calibration parameters from the launch file.");
        throw std::runtime_error("No cam calibration");
    }
}


void Node::Update () {
    cv::Mat position = orb_slam_->GetCurrentPosition();

    int trackingState = orb_slam_->GetTrackingState();
    if (!position.empty() && trackingState == 2) { // OK tracking state
        if (publish_tf_param_){
            PublishPositionAsTransform(position);
        }

        if (publish_pose_param_) {
            PublishPositionAsPoseStamped(position);
        }

        if (was_lost_){
            ROS_INFO("Successful relocalization.");
            was_lost_ = false;
        }

    } else {
        switch (trackingState) {
            case 0: ROS_WARN_THROTTLE(1,"ORB-SLAM failed: No images yet.");
                break;
            case 1: ROS_WARN_THROTTLE(1,"ORB-SLAM failed: Not initialized.");
                break;
            case 3: ROS_ERROR_THROTTLE(1,"ORB-SLAM failed: Tracking LOST.");
                break;
        }

        ROS_WARN_THROTTLE(1,"Broadcasting odometry TF from %s to %s.", target_frame_id_param_.c_str(), map_frame_id_param_.c_str());
        // Get TF from robot's odometry published topic and send to tf
        geometry_msgs::TransformStamped msg = tf2::eigenToTransform(odometry_pose_);
        msg.header.frame_id = map_frame_id_param_;
        msg.header.stamp = ros::Time::now();
        msg.header.seq += 1;
        msg.child_frame_id = target_frame_id_param_;

        // Broadcast tf
        static tf2_ros::TransformBroadcaster tf_broadcaster;
        tf_broadcaster.sendTransform(msg);

        was_lost_ = true;
    }

    PublishRenderedImage (orb_slam_->DrawCurrentFrame());

    if (publish_pointcloud_param_) {
        // Get transformation from camera optical link to base
        Eigen::Affine3d T_rt(Eigen::AngleAxisd(M_PI / 2.0, Eigen::Vector3d::UnitZ()));
        getTfTransformMatrix(T_rt, _robot_namespace_+"/camera_rgb_frame", target_frame_id_param_);
        cam_base_R_ = T_rt.rotation();
        cam_base_T_ = T_rt.translation();
        PublishMapPoints (orb_slam_->GetAllMapPoints());
    }

    PublishGBAStatus (orb_slam_->isRunningGBA());
    PublishState(trackingState);

    auto vertex_getter=orb_slam_->getVertex();
    publishVertices(vertex_getter);

    auto edges_getter=orb_slam_->getEdges();
    publishEdges(edges_getter);

    auto point_getter=orb_slam_->getMapPoints();
    publishPoints(point_getter);

}


void Node::OdomCallback(const nav_msgs::Odometry::ConstPtr& msg){

    // Translation
    Eigen::Vector3d t(msg->pose.pose.position.x,
                      msg->pose.pose.position.y,
                      msg->pose.pose.position.z);

    // Rotation
    Eigen::Quaterniond q;
    q.x() = msg->pose.pose.orientation.x;
    q.y() = msg->pose.pose.orientation.y;
    q.z() = msg->pose.pose.orientation.z;
    q.w() = msg->pose.pose.orientation.w;
    Eigen::Matrix3d R = q.normalized().toRotationMatrix();

    // Save in affine transformation
    odometry_pose_.translation() = t;
    odometry_pose_.linear() = R;

}


void Node::PublishState(int trackingState) {
     // save state from tracking, even if there are no subscribers
     orb_state_ = toORBStateMessage(trackingState);

    if (state_publisher_.getNumSubscribers() > 0) {
        // publish state as ORBState int
        orb_state_.header.stamp = ros::Time::now();
        state_publisher_.publish(orb_state_);
    }

    if (state_desc_publisher_.getNumSubscribers() > 0) {
        // publish state as string
        std_msgs::String state_desc_msg;
        state_desc_msg.data = stateDescription(orb_state_);
        state_desc_publisher_.publish(state_desc_msg);
    }

}


void Node::PublishGBAStatus (bool gba_status) {
    if (status_gba_publisher_.getNumSubscribers() > 0) {
        std_msgs::Bool gba_status_msg;
        gba_status_msg.data = gba_status;
        status_gba_publisher_.publish(gba_status_msg);
    }
}


void Node::PublishMapPoints (std::vector<ORB_SLAM2::MapPoint*> map_points) {
    sensor_msgs::PointCloud2 cloud = MapPointsToPointCloud(map_points);
    map_points_publisher_.publish(cloud);
}


void Node::PublishPositionAsTransform (cv::Mat position) {
    // Get transform from map to camera frame
    tf2::Transform tf_transform = TransformFromMat(position);

    // Make transform from camera frame to target frame
    tf2::Transform tf_map2target = TransformToTarget(tf_transform, camera_frame_id_param_, target_frame_id_param_);

    // Make message
    tf2::Stamped<tf2::Transform> tf_map2target_stamped;
    tf_map2target_stamped = tf2::Stamped<tf2::Transform>(tf_map2target, current_frame_time_, map_frame_id_param_);
    geometry_msgs::TransformStamped msg = tf2::toMsg(tf_map2target_stamped);
    msg.child_frame_id = target_frame_id_param_;
    // Broadcast tf
    static tf2_ros::TransformBroadcaster tf_broadcaster;
    tf_broadcaster.sendTransform(msg);
}


void Node::PublishPositionAsPoseStamped (cv::Mat position) {
    tf2::Transform tf_position = TransformFromMat(position);

    // Make transform from camera frame to target frame
    tf2::Transform tf_position_target = TransformToTarget(tf_position, camera_frame_id_param_, target_frame_id_param_);

    // Make message
    tf2::Stamped<tf2::Transform> tf_position_target_stamped;
    tf_position_target_stamped = tf2::Stamped<tf2::Transform>(tf_position_target, current_frame_time_, map_frame_id_param_);
    geometry_msgs::PoseStamped pose_msg;
    tf2::toMsg(tf_position_target_stamped, pose_msg);
    pose_publisher_.publish(pose_msg);
}


void Node::PublishRenderedImage (cv::Mat image) {
    if (rendered_image_publisher_.getNumSubscribers() > 0) {
        std_msgs::Header header;
        header.stamp = current_frame_time_;
        header.frame_id = map_frame_id_param_;
        const sensor_msgs::ImagePtr rendered_image_msg = cv_bridge::CvImage(header, "bgr8", image).toImageMsg();
        rendered_image_publisher_.publish(rendered_image_msg);
    }
}


const orb_slam2_ros::ORBState Node::toORBStateMessage(int trackingState)
{
    orb_slam2_ros::ORBState state_msg;
    state_msg.state = orb_slam2_ros::ORBState::UNKNOWN;

    switch (trackingState) {
        case 0: state_msg.state = orb_slam2_ros::ORBState::NO_IMAGES_YET;
            break;
        case 1: state_msg.state = orb_slam2_ros::ORBState::SYSTEM_NOT_READY;
            break;
        case 2: state_msg.state = orb_slam2_ros::ORBState::OK;
            break;
        case 3: state_msg.state = orb_slam2_ros::ORBState::LOST;
            break;
    }

    return state_msg;
}


const char* Node::stateDescription(orb_slam2_ros::ORBState orb_state)
{
    switch (orb_state.state) {
        case orb_slam2_ros::ORBState::SYSTEM_NOT_READY: return "System not ready";
        case orb_slam2_ros::ORBState::NO_IMAGES_YET: return "No images yet";
        case orb_slam2_ros::ORBState::NOT_INITIALIZED: return "Not initialized";
        case orb_slam2_ros::ORBState::OK: return "OK";
        case orb_slam2_ros::ORBState::LOST: return "Tracking lost";
    }

    return "???";
}


tf2::Transform Node::TransformToTarget (tf2::Transform tf_in, std::string frame_in, std::string frame_target) {
    // Transform tf_in from frame_in to frame_target
    tf2::Transform tf_map2orig = tf_in;
    tf2::Transform tf_orig2target;
    tf2::Transform tf_map2target;

    tf2::Stamped<tf2::Transform> transformStamped_temp;
    try {
        // Get the transform from camera to target
        geometry_msgs::TransformStamped tf_msg = tfBuffer->lookupTransform(frame_in, frame_target, ros::Time(0));
        // Convert to tf2
        tf2::fromMsg(tf_msg, transformStamped_temp);
        tf_orig2target.setBasis(transformStamped_temp.getBasis());
        tf_orig2target.setOrigin(transformStamped_temp.getOrigin());

    } catch (tf2::TransformException &ex) {
        ROS_WARN("%s",ex.what());
        //ros::Duration(1.0).sleep();
        tf_orig2target.setIdentity();
    }

    // Transform from map to target
    tf_map2target = tf_map2orig * tf_orig2target;

    /*
      // Print debug info
      double roll, pitch, yaw;
      // Print debug map2orig
      tf2::Matrix3x3(tf_map2orig.getRotation()).getRPY(roll, pitch, yaw);
      ROS_INFO("Static transform Map to Orig [%s -> %s]",
                      map_frame_id_param_.c_str(), frame_in.c_str());
      ROS_INFO(" * Translation: {%.3f,%.3f,%.3f}",
                      tf_map2orig.getOrigin().x(), tf_map2orig.getOrigin().y(), tf_map2orig.getOrigin().z());
      ROS_INFO(" * Rotation: {%.3f,%.3f,%.3f}",
                      RAD2DEG(roll), RAD2DEG(pitch), RAD2DEG(yaw));
      // Print debug tf_orig2target
      tf2::Matrix3x3(tf_orig2target.getRotation()).getRPY(roll, pitch, yaw);
      ROS_INFO("Static transform Orig to Target [%s -> %s]",
                      frame_in.c_str(), frame_target.c_str());
      ROS_INFO(" * Translation: {%.3f,%.3f,%.3f}",
                      tf_orig2target.getOrigin().x(), tf_orig2target.getOrigin().y(), tf_orig2target.getOrigin().z());
      ROS_INFO(" * Rotation: {%.3f,%.3f,%.3f}",
                      RAD2DEG(roll), RAD2DEG(pitch), RAD2DEG(yaw));
      // Print debug map2target
      tf2::Matrix3x3(tf_map2target.getRotation()).getRPY(roll, pitch, yaw);
      ROS_INFO("Static transform Map to Target [%s -> %s]",
                      map_frame_id_param_.c_str(), frame_target.c_str());
      ROS_INFO(" * Translation: {%.3f,%.3f,%.3f}",
                      tf_map2target.getOrigin().x(), tf_map2target.getOrigin().y(), tf_map2target.getOrigin().z());
      ROS_INFO(" * Rotation: {%.3f,%.3f,%.3f}",
                      RAD2DEG(roll), RAD2DEG(pitch), RAD2DEG(yaw));

     */
    return tf_map2target;
}


tf2::Transform Node::TransformFromMat (cv::Mat position_mat) {
    cv::Mat rotation(3,3,CV_32F);
    cv::Mat translation(3,1,CV_32F);

    rotation = position_mat.rowRange(0,3).colRange(0,3);
    translation = position_mat.rowRange(0,3).col(3);


    tf2::Matrix3x3 tf_camera_rotation (rotation.at<float> (0,0), rotation.at<float> (0,1), rotation.at<float> (0,2),
                                       rotation.at<float> (1,0), rotation.at<float> (1,1), rotation.at<float> (1,2),
                                       rotation.at<float> (2,0), rotation.at<float> (2,1), rotation.at<float> (2,2)
    );

    tf2::Vector3 tf_camera_translation (translation.at<float> (0), translation.at<float> (1), translation.at<float> (2));

    //Coordinate transformation matrix from orb coordinate system to ros coordinate system
    const tf2::Matrix3x3 tf_orb_to_ros (0, 0, 1,
                                        -1, 0, 0,
                                        0,-1, 0);

    //Transform from orb coordinate system to ros coordinate system on camera coordinates
    tf_camera_rotation = tf_orb_to_ros*tf_camera_rotation;
    tf_camera_translation = tf_orb_to_ros*tf_camera_translation;

    //Inverse matrix
    tf_camera_rotation = tf_camera_rotation.transpose();
    tf_camera_translation = -(tf_camera_rotation*tf_camera_translation);

    //Transform from orb coordinate system to ros coordinate system on map coordinates
    tf_camera_rotation = tf_orb_to_ros*tf_camera_rotation;
    tf_camera_translation = tf_orb_to_ros*tf_camera_translation;

    return tf2::Transform (tf_camera_rotation, tf_camera_translation);
}


sensor_msgs::PointCloud2 Node::MapPointsToPointCloud (std::vector<ORB_SLAM2::MapPoint*> map_points) {
    if (map_points.size() == 0) {
        std::cout << "Map point vector is empty!" << std::endl;
    }

    sensor_msgs::PointCloud2 cloud;

    const int num_channels = 3; // x y z

    cloud.header.stamp = current_frame_time_;
    cloud.header.frame_id = map_frame_id_param_;
    cloud.height = 1;
    cloud.width = map_points.size();
    cloud.is_bigendian = false;
    cloud.is_dense = true;
    cloud.point_step = num_channels * sizeof(float);
    cloud.row_step = cloud.point_step * cloud.width;
    cloud.fields.resize(num_channels);

    std::string channel_id[] = { "x", "y", "z"};
    for (int i = 0; i<num_channels; i++) {
        cloud.fields[i].name = channel_id[i];
        cloud.fields[i].offset = i * sizeof(float);
        cloud.fields[i].count = 1;
        cloud.fields[i].datatype = sensor_msgs::PointField::FLOAT32;
    }

    cloud.data.resize(cloud.row_step * cloud.height);

    unsigned char *cloud_data_ptr = &(cloud.data[0]);

    float data_array[num_channels];
    for (unsigned int i=0; i<cloud.width; i++) {
        if(!map_points[i])
            continue;

        if (map_points.at(i)->nObs >= min_observations_per_point_) {
            Eigen::Vector3f map_pt_f(map_points.at(i)->GetWorldPos().at<float>(0),
                                   map_points.at(i)->GetWorldPos().at<float>(1),
                                   map_points.at(i)->GetWorldPos().at<float>(2));

            Eigen::Vector3d map_pt = map_pt_f.cast<double>();

            map_pt = cam_base_R_ * map_pt;
            map_pt += cam_base_T_;

            data_array[0] = map_pt[0];
            data_array[1] = map_pt[1];
            data_array[2] = map_pt[2];

            memcpy(cloud_data_ptr + (i * cloud.point_step), data_array, num_channels * sizeof(float));
        }
    }

    return cloud;
}


void Node::ParamsChangedCallback(orb_slam2_ros::dynamic_reconfigureConfig &config, uint32_t level) {
    orb_slam_->EnableLocalizationOnly (config.localize_only);
    min_observations_per_point_ = config.min_observations_for_ros_map;

    if (config.reset_map) {
        orb_slam_->Reset();
        config.reset_map = false;
    }

    orb_slam_->SetMinimumKeyFrames (config.min_num_kf_in_map);
}


bool Node::SaveMapSrv (orb_slam2_ros::SaveMap::Request &req, orb_slam2_ros::SaveMap::Response &res) {
    res.success = orb_slam_->SaveMap(req.name);

    if (res.success) {
        ROS_INFO_STREAM ("Map was saved as " << req.name);
    } else {
        ROS_ERROR ("Map could not be saved.");
    }

    return res.success;
}


bool Node::getTfTransformMatrix(Eigen::Affine3d &transform_matrix, const std::string source_frame, const std::string target_frame) {
    try{
        geometry_msgs::TransformStamped transform_to_robot = tfBuffer->lookupTransform(target_frame, source_frame,ros::Time::now(),ros::Duration(0.05));

        transform_matrix = tf2::transformToEigen(transform_to_robot);
        return true;
    }
    catch (tf2::TransformException &ex){
        ROS_WARN("%s",ex.what());
        return false;
    }
}


void Node::publishVertices(std::list<float>& l){
    std_msgs::Float64MultiArray msg;
    msg.layout.dim.push_back(std_msgs::MultiArrayDimension());
    msg.layout.data_offset = 0;
    msg.layout.dim[0].size = l.size();
    msg.layout.dim[0].stride = 8; // ID1, quaternion, position

    for(float f : l){
        msg.data.push_back(f);
    }

    vertex_publisher_.publish(msg);
}


void Node::publishEdges(std::list<float>& l){
    std_msgs::Float64MultiArray msg;
    msg.layout.dim.push_back(std_msgs::MultiArrayDimension());
    msg.layout.data_offset = 0;
    msg.layout.dim[0].size = l.size();
    msg.layout.dim[0].stride = 38; // ID1, ID2, Hessian (6x6)

    for(float f : l){
        msg.data.push_back(f);
    }

    edge_publisher_.publish(msg);
}


void Node::publishPoints(std::list<float>& l){
    std_msgs::Float64MultiArray msg;
    msg.layout.dim.push_back(std_msgs::MultiArrayDimension());
    msg.layout.data_offset = 0;
    msg.layout.dim[0].size = l.size();

    // Array of unknown size since the number of observation varies

    for(float f : l){
        msg.data.push_back(f);
    }

    point_publisher_.publish(msg);
}