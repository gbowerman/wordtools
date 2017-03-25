FROM mysql
COPY createdb.sql /docker-entrypoint-initdb.d/
COPY en.csv /var/lib/mysql-files/
RUN sed -i "s/.*bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/my.cnf