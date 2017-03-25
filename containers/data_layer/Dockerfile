FROM mysql
COPY fix-permissions.sh /docker-entrypoint-initdb.d/fix-permissions.sh
RUN chmod +x /docker-entrypoint-initdb.d/fix-permissions.sh
COPY createdb.sql /docker-entrypoint-initdb.d/
COPY en.csv /var/lib/mysql-files/
