FROM postgres:9.6
ADD database.sql /docker-entrypoint-initdb.d/db.sql
