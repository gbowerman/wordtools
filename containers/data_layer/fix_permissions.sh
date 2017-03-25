#!/bin/bash
mysql -u root -p${MYSQL_ROOT_PASSWORD} -e "grant all on worddb.* to '${MYSQL_USER}'@'%' identified by '${MYSQL_PASSWORD}'; flush privileges;"