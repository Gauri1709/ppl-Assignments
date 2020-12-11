(print (defun m(n li)
      (if (zerop n)
         (first li)
         (m (- n 1)(rest li)))))

