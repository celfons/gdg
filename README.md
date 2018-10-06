* Simulação de um micro serviço:

- Containers separados no compose

- Kafka + Zookeeper

- Python Rest com base Mongo para leitura e produtor kafka

- Kotlin Consumidor Kafka com base Postresql para escrita


* USO:

- docker-compose build

- docker-compose up

- POST 0.0.0.0:8000
[
    {
      "name": "marcel",
       "message":"ok"
    }
]

- GET 0.0.0.0:8000

* postgresql

- user:root
- password:123
