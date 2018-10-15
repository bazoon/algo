
(defvar x #b1000000111111111)

; (setf x 333444)



; (print (logbitp 0 x))

; (print (format nil "~b" x))
; (print (integer-length x) )

(dotimes (i (ceiling (integer-length x)) 7) (print i))

; (print (format nil "~b" (ldb (byte 8 8) x) ))