(defn hello_word_n_times[n]
    (dotimes [i n] (println "Hello World"))
)


(def n (Integer/parseInt (read-line)))
(hello_word_n_times n)
