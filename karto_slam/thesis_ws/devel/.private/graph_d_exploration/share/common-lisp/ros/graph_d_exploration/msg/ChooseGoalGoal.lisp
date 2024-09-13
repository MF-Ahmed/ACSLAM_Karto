; Auto-generated. Do not edit!


(cl:in-package graph_d_exploration-msg)


;//! \htmlinclude ChooseGoalGoal.msg.html

(cl:defclass <ChooseGoalGoal> (roslisp-msg-protocol:ros-message)
  ((client_id
    :reader client_id
    :initarg :client_id
    :type cl:string
    :initform "")
   (matrix
    :reader matrix
    :initarg :matrix
    :type graph_d_exploration-msg:InfoMatrix
    :initform (cl:make-instance 'graph_d_exploration-msg:InfoMatrix))
   (rows
    :reader rows
    :initarg :rows
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass ChooseGoalGoal (<ChooseGoalGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChooseGoalGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChooseGoalGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name graph_d_exploration-msg:<ChooseGoalGoal> is deprecated: use graph_d_exploration-msg:ChooseGoalGoal instead.")))

(cl:ensure-generic-function 'client_id-val :lambda-list '(m))
(cl:defmethod client_id-val ((m <ChooseGoalGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graph_d_exploration-msg:client_id-val is deprecated.  Use graph_d_exploration-msg:client_id instead.")
  (client_id m))

(cl:ensure-generic-function 'matrix-val :lambda-list '(m))
(cl:defmethod matrix-val ((m <ChooseGoalGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graph_d_exploration-msg:matrix-val is deprecated.  Use graph_d_exploration-msg:matrix instead.")
  (matrix m))

(cl:ensure-generic-function 'rows-val :lambda-list '(m))
(cl:defmethod rows-val ((m <ChooseGoalGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graph_d_exploration-msg:rows-val is deprecated.  Use graph_d_exploration-msg:rows instead.")
  (rows m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChooseGoalGoal>) ostream)
  "Serializes a message object of type '<ChooseGoalGoal>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'client_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'client_id))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'matrix) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'rows))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    ))
   (cl:slot-value msg 'rows))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChooseGoalGoal>) istream)
  "Deserializes a message object of type '<ChooseGoalGoal>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'client_id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'client_id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'matrix) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'rows) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'rows)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChooseGoalGoal>)))
  "Returns string type for a message object of type '<ChooseGoalGoal>"
  "graph_d_exploration/ChooseGoalGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChooseGoalGoal)))
  "Returns string type for a message object of type 'ChooseGoalGoal"
  "graph_d_exploration/ChooseGoalGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChooseGoalGoal>)))
  "Returns md5sum for a message object of type '<ChooseGoalGoal>"
  "ccc4eb8941602a0039260071e46f98e1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChooseGoalGoal)))
  "Returns md5sum for a message object of type 'ChooseGoalGoal"
  "ccc4eb8941602a0039260071e46f98e1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChooseGoalGoal>)))
  "Returns full string definition for message of type '<ChooseGoalGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Action definition for choosing centroids~%# The goal specifies the client id and the matrix with the lists in which each element is of the form [Reward, X, Y]~%# The action server should try to choose the centroid that maximizes the information gain depending on the priority~%# of the robots (r0 > ... > rn)~%~%# Goal definition~%string client_id~%InfoMatrix matrix~%int8[] rows~%~%================================================================================~%MSG: graph_d_exploration/InfoMatrix~%# Matrix of type [Reward, X, Y] with dimensions [nx3]~%uint32 rows~%float32[] data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChooseGoalGoal)))
  "Returns full string definition for message of type 'ChooseGoalGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Action definition for choosing centroids~%# The goal specifies the client id and the matrix with the lists in which each element is of the form [Reward, X, Y]~%# The action server should try to choose the centroid that maximizes the information gain depending on the priority~%# of the robots (r0 > ... > rn)~%~%# Goal definition~%string client_id~%InfoMatrix matrix~%int8[] rows~%~%================================================================================~%MSG: graph_d_exploration/InfoMatrix~%# Matrix of type [Reward, X, Y] with dimensions [nx3]~%uint32 rows~%float32[] data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChooseGoalGoal>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'client_id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'matrix))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'rows) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChooseGoalGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'ChooseGoalGoal
    (cl:cons ':client_id (client_id msg))
    (cl:cons ':matrix (matrix msg))
    (cl:cons ':rows (rows msg))
))
