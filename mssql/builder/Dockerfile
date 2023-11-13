FROM mcr.microsoft.com/mssql/server:2022-latest


WORKDIR /data

COPY migrate.sh .

USER root
RUN chmod +x migrate.sh

RUN sed -i 's/\r$//' /data/migrate.sh

