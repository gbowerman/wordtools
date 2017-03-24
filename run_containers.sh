#!/bin/bash
# run containers
cd containers
cd data_layer
docker run -d -t --network=host -p 3306:3306 -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD  -e MYSQL_USER=worduser -e MYSQL_PASSWORD=$MYSQL_PASSWORD -e MYSQL_DATABASE=worddb wordtools_data
cd ../api_layer
docker run -d -t --network=host -p 8081:8081 -e MYSQL_PASSWORD=$MYSQL_PASSWORD wordtools_api
cd ../presentation_layer
docker run -d -t --network=host -p 8080:8080 wordtools_presentation
cd ../..