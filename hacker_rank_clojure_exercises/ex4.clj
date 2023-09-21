(defn printValuesLessThan [delimiter lst]
  (doseq [number lst]
         (if (< number delimiter) (println number))
  )
)
