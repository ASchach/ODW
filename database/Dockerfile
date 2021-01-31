FROM mysql:latest
ENV MYSQL_ALLOW_EMPTY_PASSWORD YES

COPY init.sql /docker-entrypoint-initdb.d/
