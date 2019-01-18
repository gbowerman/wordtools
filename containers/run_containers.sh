#!/bin/bash

# check for required environement variables, then run docker-compose
[ -z "$MYSQL_USER" ] && echo "Need to set environment variable MYSQL_USER" && exit 1;
[ -z "$MYSQL_PASSWORD" ] && echo "Need to set environment variable MYSQL_PASSWORD" && exit 1;
[ -z "$MYSQL_ROOT_PASSWORD" ] && echo "Need to set environment variable MYSQL_ROOT_PASSWORD" && exit 1;
[ -z "$MYSQL_DATABASE" ] && echo "Need to set environment variable MYSQL_DATABASE" && exit 1;
docker-compose up -d

# run containers standalone on host network - not required if using docker-compose
docker run -d -t --network=host -p 3306:3306 -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD  -e MYSQL_USER=worduser -e MYSQL_PASSWORD=$MYSQL_PASSWORD -e MYSQL_DATABASE=worddb sendmarsh/wordtools-data
docker run -d -t --network=host -p 8081:8081 -e MYSQL_PASSWORD=$MYSQL_PASSWORD sendmarsh/wordtools-api
docker run -d -t --network=host -p 8080:8080 sendmarsh/wordtools-presentation