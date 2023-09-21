(defn printInOddIndexes [lst]
  (def lenght (count lst))
  (def i 1)
  (while (< i lenght) (println (nth lst i)) (def i (+ i 2)))
)
