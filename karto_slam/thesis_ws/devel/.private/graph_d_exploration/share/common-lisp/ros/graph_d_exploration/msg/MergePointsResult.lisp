; Auto-generated. Do not edit!


(cl:in-package graph_d_exploration-msg)


;//! \htmlinclude MergePointsResult.msg.html

(cl:defclass <MergePointsResult> (roslisp-msg-protocol:ros-message)
  ((merged_points
    :reader merged_points
    :initarg :merged_points
    :type (cl:vector graph_d_exploration-msg:Point2D)
   :initform (cl:make-array 0 :element-type 'graph_d_exploration-msg:Point2D :initial-element (cl:make-instance 'graph_d_exploration-msg:Point2D)))
   (radius_used
    :reader radius_used
    :initarg :radius_used
    :type cl:float
    :initform 0.0)
   (percentage_used
    :reader percentage_used
    :initarg :percentage_used
    :type cl:float
    :initform 0.0))
)

(cl:defclass MergePointsResult (<MergePointsResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MergePointsResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MergePointsResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name graph_d_exploration-msg:<MergePointsResult> is deprecated: use graph_d_exploration-msg:MergePointsResult instead.")))

(cl:ensure-generic-function 'merged_points-val :lambda-list '(m))
(cl:defmethod merged_points-val ((m <MergePointsResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graph_d_exploration-msg:merged_points-val is deprecated.  Use graph_d_exploration-msg:merged_points instead.")
  (merged_points m))

(cl:ensure-generic-function 'radius_used-val :lambda-list '(m))
(cl:defmethod radius_used-val ((m <MergePointsResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graph_d_exploration-msg:radius_used-val is deprecated.  Use graph_d_exploration-msg:radius_used instead.")
  (radius_used m))

(cl:ensure-generic-function 'percentage_used-val :lambda-list '(m))
(cl:defmethod percentage_used-val ((m <MergePointsResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graph_d_exploration-msg:percentage_used-val is deprecated.  Use graph_d_exploration-msg:percentage_used instead.")
  (percentage_used m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MergePointsResult>) ostream)
  "Serializes a message object of type '<MergePointsResult>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'merged_points))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'merged_points))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'radius_used))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'percentage_used))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MergePointsResult>) istream)
  "Deserializes a message object of type '<MergePointsResult>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'merged_points) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'merged_points)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'graph_d_exploration-msg:Point2D))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'radius_used) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'percentage_used) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MergePointsResult>)))
  "Returns string type for a message object of type '<MergePointsResult>"
  "graph_d_exploration/MergePointsResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MergePointsResult)))
  "Returns string type for a message object of type 'MergePointsResult"
  "graph_d_exploration/MergePointsResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MergePointsResult>)))
  "Returns md5sum for a message object of type '<MergePointsResult>"
  "5567672ae4c3263cec809b91db7a6653")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MergePointsResult)))
  "Returns md5sum for a message object of type 'MergePointsResult"
  "5567672ae4c3263cec809b91db7a6653")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MergePointsResult>)))
  "Returns full string definition for message of type '<MergePointsResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the action result message~%Point2D[] merged_points~%float32 radius_used~%float32 percentage_used~%~%================================================================================~%MSG: graph_d_exploration/Point2D~%# Point for centroids~%float32 x~%float32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MergePointsResult)))
  "Returns full string definition for message of type 'MergePointsResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the action result message~%Point2D[] merged_points~%float32 radius_used~%float32 percentage_used~%~%================================================================================~%MSG: graph_d_exploration/Point2D~%# Point for centroids~%float32 x~%float32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MergePointsResult>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'merged_points) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MergePointsResult>))
  "Converts a ROS message object to a list"
  (cl:list 'MergePointsResult
    (cl:cons ':merged_points (merged_points msg))
    (cl:cons ':radius_used (radius_used msg))
    (cl:cons ':percentage_used (percentage_used msg))
))
