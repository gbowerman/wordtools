# worddb - Word finder database

A set of scripts to generate a MySQL database consisting of an indexed list of words, with word length

### Setup

1. Install MySQL
2. Download files
2. Run _gen_word_data.sh_ which will download a word list and convert it to the required CSV file
3. Run the .SQL file to create and load the database: mysql -u root -p worddb < createdb.sql