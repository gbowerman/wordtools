
# Word finder

This app provides web-based word finding tools, and consists of:
- Database layer - an indexed word dictionary, implemented with MySQL.
- API layer - providing word search, anagram, random word functions via a REST API, implemented with Python Bottle micro-web framework.
- Presentation layer - web UI which calls the API layer, also implemented with Bottle.

There are more efficient ways to load and index a dictionary style list of words than to use a database server, but he purpose of this app is more to demonstrate a simple micro-service architecture. Each layer is easy to implement as a container, and can be deployed as a set of inter-related containers in a pod.

### Installation

More detailed instructions are in-progress..

  1. Install Python 3.x. with Bottle, pymysql
  2. Install MySQL database server.
  3. Import the worddb database.
  4. Put database user/password details in the dbconfig.json file.
  5. Deploy with ./deploy.sh
  6. Connect to the web UI endpoint, e.g. http://localhost:8080
  7. Shutdown app with ./killjobs.sh
 