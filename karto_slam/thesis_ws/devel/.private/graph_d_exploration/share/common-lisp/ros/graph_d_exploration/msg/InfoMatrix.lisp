; Auto-generated. Do not edit!


(cl:in-package graph_d_exploration-msg)


;//! \htmlinclude InfoMatrix.msg.html

(cl:defclass <InfoMatrix> (roslisp-msg-protocol:ros-message)
  ((rows
    :reader rows
    :initarg :rows
    :type cl:integer
    :initform 0)
   (data
    :reader data
    :initarg :data
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass InfoMatrix (<InfoMatrix>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <InfoMatrix>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'InfoMatrix)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name graph_d_exploration-msg:<InfoMatrix> is deprecated: use graph_d_exploration-msg:InfoMatrix instead.")))

(cl:ensure-generic-function 'rows-val :lambda-list '(m))
(cl:defmethod rows-val ((m <InfoMatrix>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graph_d_exploration-msg:rows-val is deprecated.  Use graph_d_exploration-msg:rows instead.")
  (rows m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <InfoMatrix>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader graph_d_exploration-msg:data-val is deprecated.  Use graph_d_exploration-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <InfoMatrix>) ostream)
  "Serializes a message object of type '<InfoMatrix>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rows)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rows)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'rows)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'rows)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <InfoMatrix>) istream)
  "Deserializes a message object of type '<InfoMatrix>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'rows)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'rows)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'rows)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'rows)) (cl:read-byte istream))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<InfoMatrix>)))
  "Returns string type for a message object of type '<InfoMatrix>"
  "graph_d_exploration/InfoMatrix")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'InfoMatrix)))
  "Returns string type for a message object of type 'InfoMatrix"
  "graph_d_exploration/InfoMatrix")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<InfoMatrix>)))
  "Returns md5sum for a message object of type '<InfoMatrix>"
  "c56ec7891acf134bf7f478b29ade73c5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'InfoMatrix)))
  "Returns md5sum for a message object of type 'InfoMatrix"
  "c56ec7891acf134bf7f478b29ade73c5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<InfoMatrix>)))
  "Returns full string definition for message of type '<InfoMatrix>"
  (cl:format cl:nil "# Matrix of type [Reward, X, Y] with dimensions [nx3]~%uint32 rows~%float32[] data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'InfoMatrix)))
  "Returns full string definition for message of type 'InfoMatrix"
  (cl:format cl:nil "# Matrix of type [Reward, X, Y] with dimensions [nx3]~%uint32 rows~%float32[] data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <InfoMatrix>))
  (cl:+ 0
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <InfoMatrix>))
  "Converts a ROS message object to a list"
  (cl:list 'InfoMatrix
    (cl:cons ':rows (rows msg))
    (cl:cons ':data (data msg))
))
