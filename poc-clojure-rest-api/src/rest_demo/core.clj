(ns rest-demo.core
  (:require [org.httpkit.server :as server]
            [org.httpkit.client :as http]
            [compojure.core :refer :all]
            [compojure.route :as route]
            [ring.middleware.defaults :refer :all]
            [clojure.pprint :as pp]
            [clojure.string :as str]
            [clojure.data.json :as json])
  (:gen-class))


; Simple Body Page
(defn simple-body-page [req]
  {:status  200
   :headers {"Content-Type" "text/html"}
   :body    "Hello World"})

; request-example
(defn request-example [req]
     {:status  200
      :headers {"Content-Type" "text/html"}
      :body    (->>
                (pp/pprint req)
                (str "Request Object: " req))})


(comment (def options {:timeout 200             ; ms
              :basic-auth ["user" "pass"]
              :query-params {:param "value" :param2 ["value1" "value2"]}
              :user-agent "User-Agent-string"
              :headers {"X-Header" "Value"}}))

(defn handle-response [{:keys [status headers body error opts]}]
  ({:status status
   :headers {"Content-Type" "text/html"}
   :body body}))

(defn make-request [req]
     {:status  200
      :headers {"Content-Type" "text/html"}
;      :body    (->> (http/get "http://google.com.br" handle-response))})
      :body    (->> (let [{:keys [status headers body error] :as resp} @(http/get "http://google.com.br")]
                  (if error
                  (println "Failed, exception: " error)
                  (str body))))})


(defroutes app-routes
  (GET "/" [] simple-body-page)
  (GET "/request" [] request-example)
  (GET "/make" [] make-request)
  (route/not-found "Error, page not found!")
)

(defn -main
  "This is our main entry point"
  [& args]
  (let [port (Integer/parseInt (or (System/getenv "PORT") "3000"))]
    ; Run the server with Ring.defaults middleware
    (server/run-server (wrap-defaults #'app-routes site-defaults) {:port port})
    ; Run the server without ring defaults
    ;(server/run-server #'app-routes {:port port})
    (println (str "Running webserver at http:/127.0.0.1:" port "/"))))

