**PROJECTS DONE USING APACHE KAFKA**

* To begin with, first download Apache kafka at
https://kafka.apache.org/downloads
then install it. 

    It is a cross-platform application; meaning the setup can be installed on Windows, Linux or MacOS environment.
    Unzip the downloaded file to your Drive C:

* Navigate to the kafka directory/folder and open command prompt / terminal.
 - Start the zookeeper service:
    
    - **Windows**: \bin\windows\zookeeper-server-start.bat \config\zookeeper.properties
    - **Linux**: bin/zookeeper-server-start.sh config/zookeeper.properties


 - Start the kafka server:
    - **Windows**:  \bin\windows\kafka-server-start.bat \config\server.properties
    - **Linux**: bin/kafka-server-start.sh config/server.properties
 

 - Create a topic :
    - **Windows**: \bin\windows\kafka-topics.bat --create --topic my_topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
    - **Linux**: bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

 
 - You can list all topics created using this command:
    - **Windows**: \bin\windows\kafka-topics.bat --zookeeper localhost:2181 --list
    - **Linux**: kafka-topics.sh --zookeeper localhost:2181 --list
   

 - Write some events to the topic
    - **Windows**: \bin\windows\kafka-console-producer.bat --topic my_topic --bootstrap-server localhost:9092
    - **Linux**: bin/kafka-console-producer.sh --topic my_topic --bootstrap-server localhost:9092
   

 - Suscribe / read  events from topic:
    - **Windows**: \bin\windows\kafka-console-consumer.bat --topic my_topic --from-beginning --bootstrap-server localhost:9092
    - **Linux**: bin/kafka-console-consumer.sh --topic my_topic --from-beginning --bootstrap-server localhost:9092
    

