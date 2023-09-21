(defn printTimes[num lst]
  (doseq [thisNumber lst] (dotimes [i num] (println thisNumber)))
)

(def a (Integer/parseInt (read-line)))
(def listToPrint [])

(def listToPrint (conj listToPrint (Integer/parseInt (read-line))))

(def flag 0)
(while (= flag 0)
  (def new_input (read-line))
  (if (or (= new_input "") (= new_input nil)) (def flag 1) (def listToPrint (conj listToPrint (Integer/parseInt new_input))))
)

(printTimes a listToPrint)
