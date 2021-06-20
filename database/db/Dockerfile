FROM postgres:latest
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB docker
ADD ./sql_sripts/ddl_create_tables.sql:/docker-entrypoint-initdb.d/ddl_create_tables.sql
