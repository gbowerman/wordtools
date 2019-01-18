# kill running containers
docker-compose stop
docker-compose rm --force
docker rmi sendmarsh/wordtools-data
docker rmi sendmarsh/wordtools-api
docker rmi sendmarsh/wordtools-presentation
docker rmi --force \$(docker ps -a -q)
