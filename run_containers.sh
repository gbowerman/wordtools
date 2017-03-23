# run containers
cd containers
cd data_layer
docker run -d -t -p 3306:3306 -e MYSQL_ROOT_PASSWORD=SqlD0ckerTest  -e MYSQL_USER=W0rdApp,User01 -e MYSQL_DATABASE=worddb wordtools_data
cd ../api_layer
docker run -d -t --network=host -p 8081:8081 wordtools_api
cd ../presentation_layer
docker run -d -t --network=host -p 8080:8080 wordtools_presentation
cd ../..