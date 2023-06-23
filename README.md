# Event-Driven with Python and Kafka

This repository is based on LiveProject in [Manning](https://www.manning.com/liveprojectseries/data-pipeline-ser)

## Part 1 - Python and Kafka

Using this [docker-compose](https://github.com/bitnami/containers/blob/e1f4cfea7b1d7666c620242ed61cc20cb32f3b69/bitnami/kafka/docker-compose.yml)

Check connection to Kafka

```bash
nc -zv localhost 9092
```
Check connection to Zookeeper

```bash
nc -zv localhost 2181
```

Producer

```bash
docker-compose exec -it kafka /opt/bitnami/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --producer.config /opt/bitnami/kafka/config/producer.properties --topic test
```

Consumer

```bash
docker-compose exec -it kafka /opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test
```

## Part 2 - Observability

Produce message in topic in file hello_word.py. After send we specify the topic and message.

```bash
poetry run faust -A hello_world send hello "Hello Kafka topic"   
poetry run faust -A hello_world send greeting "Greeting Kafka topic2222222" 
```

Start worker

```bash
 poetry run faust -A hello_world worker -l info
```

## Part 3 - Automate Reports