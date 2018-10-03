Simulação de um micro serviço:

1- Containers separados no compose

2- Kafka + Zookeeper

3- Python Rest com base Mongo para leitura e produtor kafka

4- Kotlin Consumidor Kafka com base Postresql para escrita


USO:

docker-compose build

docker-compose up

POST 0.0.0.0:8000
[
    {
      "name": "marcel",
       "value":"ok"
    }
]

GET 0.0.0.0:8000

postgresql

user:root
password:123