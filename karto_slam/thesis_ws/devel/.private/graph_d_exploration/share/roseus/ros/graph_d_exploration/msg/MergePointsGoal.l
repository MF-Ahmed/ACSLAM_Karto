;; Auto-generated. Do not edit!


(when (boundp 'graph_d_exploration::MergePointsGoal)
  (if (not (find-package "GRAPH_D_EXPLORATION"))
    (make-package "GRAPH_D_EXPLORATION"))
  (shadow 'MergePointsGoal (find-package "GRAPH_D_EXPLORATION")))
(unless (find-package "GRAPH_D_EXPLORATION::MERGEPOINTSGOAL")
  (make-package "GRAPH_D_EXPLORATION::MERGEPOINTSGOAL"))

(in-package "ROS")
;;//! \htmlinclude MergePointsGoal.msg.html


(defclass graph_d_exploration::MergePointsGoal
  :super ros::object
  :slots (_client_id _points ))

(defmethod graph_d_exploration::MergePointsGoal
  (:init
   (&key
    ((:client_id __client_id) "")
    ((:points __points) ())
    )
   (send-super :init)
   (setq _client_id (string __client_id))
   (setq _points __points)
   self)
  (:client_id
   (&optional __client_id)
   (if __client_id (setq _client_id __client_id)) _client_id)
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
    ;; string _client_id
    4 (length _client_id)
    ;; graph_d_exploration/Point2D[] _points
    (apply #'+ (send-all _points :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _client_id
       (write-long (length _client_id) s) (princ _client_id s)
     ;; graph_d_exploration/Point2D[] _points
     (write-long (length _points) s)
     (dolist (elem _points)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _client_id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _client_id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; graph_d_exploration/Point2D[] _points
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _points (let (r) (dotimes (i n) (push (instance graph_d_exploration::Point2D :init) r)) r))
     (dolist (elem- _points)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get graph_d_exploration::MergePointsGoal :md5sum-) "63e476301d9f3c67c68b09ab685fcd2b")
(setf (get graph_d_exploration::MergePointsGoal :datatype-) "graph_d_exploration/MergePointsGoal")
(setf (get graph_d_exploration::MergePointsGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Define a message type for passing an array of points to the server and getting the merged points back

# Define the action goal message
string client_id
Point2D[] points

================================================================================
MSG: graph_d_exploration/Point2D
# Point for centroids
float32 x
float32 y
")



(provide :graph_d_exploration/MergePointsGoal "63e476301d9f3c67c68b09ab685fcd2b")


