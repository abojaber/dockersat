ARG ELASTIC_VERSION

# https://www.docker.elastic.co/
FROM docker.elastic.co/logstash/logstash:${ELASTIC_VERSION}



## 
# you may download logstash-plugin in .config file before install them
# TODO:// write docs

#COPY ./config/mssql-jdbc-7.0.0.jre8.jar /usr/share/logstash/sqljdbc_7.0/enu/mssql-jdbc-7.0.0.jre8.jar

#COPY ./config/logstash-output-mongodb-3.1.5.gem /
#RUN chown -R logstash:logstash /logstash-output-mongodb-3.1.5.gem
#RUN chmod 755 /logstash-output-mongodb-3.1.5.gem
#RUN /usr/share/logstash/bin/logstash-plugin install --no-verify /logstash-output-mongodb-3.1.5.gem
