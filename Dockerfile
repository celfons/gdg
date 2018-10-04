FROM postgres:9.6
COPY database.sql /docker-entrypoint-initdb.d/db.sql
