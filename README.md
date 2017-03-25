
# Word finder

This app provides web-based word finding tools, and consists of:
- Database layer - an indexed word dictionary, implemented with MySQL.
- API layer - providing word search, anagram, random word functions via a REST API, implemented with Python Bottle micro-web framework.
- Presentation layer - web UI which calls the API layer, also implemented with Bottle.

There are more efficient ways to load and index a dictionary style list of words than to use a database server, but the purpose of this app is to demonstrate a simple micro-service architecture. Each layer is implemented as a container, can be deployed as a set of inter-related containers in a pod, and scaled horizontally as needed.

To run the app you can simply download _docker-compose.yml_ and run _docker-compose up -d_ to get the containers from Docker Hub and run them. Alternatively you can adapt the build script and Dockerfiles for your own purposes and create your own app.

### Installation

Tested on an Ubuntu 16.04-LTS VM. 

  1. Optional - Install Python 3.x (if you plan to build the containers). 
  2. Install Docker and docker-compose.
  3. Clone repo, or just copy the docker-compose.yaml file if you don't plan to build the containers.
  4. Set $MYSQL_ROOT_PASSWORD $MYSQL_DATABASE, $MYSQL_USER and $MYSQL_PASSWORD environment variables (use setenv.sh.tmlp as a template).
      export MYSQL_DATABASE=worddb
      export MYSQL_USER=worduser
      export MYSQL_PASSWORD=set-a-password-of-your-choice-here
      export MYSQL_ROOT_PASSWORD=set-a-password-ofyour-choice-here
      
  4. Optional - Run: bash ./build_containers.sh - this builds and pushes the containers. Edit the file for your docker hub account.
  5. Run: docker-compose up -d
  6. Connect to the web UI endpoint, e.g. http://yourvmdns:8080
  7. Shutdown app with: docker-compose stop
 