# Отчет по ДЗ_5

1. Создать Dockerfile с установкой Spark и Python (5 баллов).
```
FROM apache/spark:3.5.0

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    pip3 install --no-cache-dir pyspark && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
```
2. Собрать образ Docker (5 баллов).
```
services:
  spark:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: spark_python
    volumes:
      - ./app:/app
    command: ["python3", "wordcount.py"]
```
запуск контейнера
```
docker compose up
```
3. Запустить контейнер с монтированием вашей директории (5 баллов).
в компоуз файле указано
4. Выполнить пример Spark-приложения (5 баллов).
результат выполнения команды command: ["python3", "wordcount.py"]

```
spark_python  | Word counts:
spark_python  | hello: 3
spark_python  | is: 1
spark_python  | world: 2
spark_python  | again: 1
spark_python  | pyspark: 2
spark_python  | great: 1
```