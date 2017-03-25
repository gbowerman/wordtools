FROM mysql
COPY fix_permissions.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/fix_permissions.sh
COPY createdb.sql /docker-entrypoint-initdb.d/
COPY en.csv /var/lib/mysql-files/
