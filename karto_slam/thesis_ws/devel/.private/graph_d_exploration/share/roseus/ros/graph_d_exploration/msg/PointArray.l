;; Auto-generated. Do not edit!


(when (boundp 'graph_d_exploration::PointArray)
  (if (not (find-package "GRAPH_D_EXPLORATION"))
    (make-package "GRAPH_D_EXPLORATION"))
  (shadow 'PointArray (find-package "GRAPH_D_EXPLORATION")))
(unless (find-package "GRAPH_D_EXPLORATION::POINTARRAY")
  (make-package "GRAPH_D_EXPLORATION::POINTARRAY"))

(in-package "ROS")
;;//! \htmlinclude PointArray.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass graph_d_exploration::PointArray
  :super ros::object
  :slots (_points ))

(defmethod graph_d_exploration::PointArray
  (:init
   (&key
    ((:points __points) ())
    )
   (send-super :init)
   (setq _points __points)
   self)
  (:points
   (&rest __points)
   (if (keywordp (car __points))
       (send* _points __points)
     (progn
       (if __points (setq _points (car __points)))
       _points)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point[] _points
    (apply #'+ (send-all _points :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point[] _points
     (write-long (length _points) s)
     (dolist (elem _points)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point[] _points
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _points (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _points)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get graph_d_exploration::PointArray :md5sum-) "3fb3f9dacc279b964c4c8341122c34df")
(setf (get graph_d_exploration::PointArray :datatype-) "graph_d_exploration/PointArray")
(setf (get graph_d_exploration::PointArray :definition-)
      "# An array of points

geometry_msgs/Point[] points

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :graph_d_exploration/PointArray "3fb3f9dacc279b964c4c8341122c34df")


