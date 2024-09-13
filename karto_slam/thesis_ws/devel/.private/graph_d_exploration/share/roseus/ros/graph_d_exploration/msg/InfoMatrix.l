;; Auto-generated. Do not edit!


(when (boundp 'graph_d_exploration::InfoMatrix)
  (if (not (find-package "GRAPH_D_EXPLORATION"))
    (make-package "GRAPH_D_EXPLORATION"))
  (shadow 'InfoMatrix (find-package "GRAPH_D_EXPLORATION")))
(unless (find-package "GRAPH_D_EXPLORATION::INFOMATRIX")
  (make-package "GRAPH_D_EXPLORATION::INFOMATRIX"))

(in-package "ROS")
;;//! \htmlinclude InfoMatrix.msg.html


(defclass graph_d_exploration::InfoMatrix
  :super ros::object
  :slots (_rows _data ))

(defmethod graph_d_exploration::InfoMatrix
  (:init
   (&key
    ((:rows __rows) 0)
    ((:data __data) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _rows (round __rows))
   (setq _data __data)
   self)
  (:rows
   (&optional __rows)
   (if __rows (setq _rows __rows)) _rows)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; uint32 _rows
    4
    ;; float32[] _data
    (* 4    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _rows
       (write-long _rows s)
     ;; float32[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (sys::poke (elt _data i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _rows
     (setq _rows (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get graph_d_exploration::InfoMatrix :md5sum-) "c56ec7891acf134bf7f478b29ade73c5")
(setf (get graph_d_exploration::InfoMatrix :datatype-) "graph_d_exploration/InfoMatrix")
(setf (get graph_d_exploration::InfoMatrix :definition-)
      "# Matrix of type [Reward, X, Y] with dimensions [nx3]
uint32 rows
float32[] data
")



(provide :graph_d_exploration/InfoMatrix "c56ec7891acf134bf7f478b29ade73c5")


