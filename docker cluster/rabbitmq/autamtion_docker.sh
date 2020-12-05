docker run -d --net rabbits -v ${PWD}/config/rabbit-1/:/config/ -e RABBITMQ_CONFIG_FILE=/config/rabbitmq -e RABBITMQ_ERLANG_COOKIE=WIWVHCDTCIUAWANLMQAW --hostname rabbit-1 --name rabbit-1 -p 8081:15672 rabbitmq:3.8-management

docker run -d --net rabbits -v ${PWD}/config/rabbit-2/:/config/ -e RABBITMQ_CONFIG_FILE=/config/rabbitmq -e RABBITMQ_ERLANG_COOKIE=WIWVHCDTCIUAWANLMQAW --hostname rabbit-2 --name rabbit-2 -p 8082:15672 rabbitmq:3.8-management

docker run -d  --net rabbits -v ${PWD}/config/rabbit-3/:/config/ -e RABBITMQ_CONFIG_FILE=/config/rabbitmq -e RABBITMQ_ERLANG_COOKIE=WIWVHCDTCIUAWANLMQAW --hostname rabbit-3 --name rabbit-3 -p 8083:15672 rabbitmq:3.8-management

#NODE 1 : MANAGEMENT http://localhost:8081
#NODE 2 : MANAGEMENT http://localhost:8082
#NODE 3 : MANAGEMENT http://localhost:8083

# enable federation plugin
docker container exec -it rabbit-1 rabbitmq-plugins enable rabbitmq_federation
docker container exec -it rabbit-2 rabbitmq-plugins enable rabbitmq_federation
docker container exec -it rabbit-3 rabbitmq-plugins enable rabbitmq_federation