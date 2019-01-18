#!/bin/bash
# reset script - deletes all docker images and resets service 
#  - only use if docker or docker-compose are acting weird 
docker stop $(docker ps -q)
sudo docker rm $(docker ps -aa -q)
sudo docker rmi $(docker images -q)
sudo systemctl restart docker