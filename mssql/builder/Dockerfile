FROM mcr.microsoft.com/mssql/server:2022-latest


WORKDIR /data

COPY migrate.sh .

COPY scripts.sql .

USER root
RUN chmod +x migrate.sh

RUN sed -i 's/\r$//' /data/migrate.sh

RUN /data/migrate.sh scripts
