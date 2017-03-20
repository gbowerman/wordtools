-- MySQL database script to generate the worddb database 
-- Assumes a local file called en.csv containing a comma seperated list which looks like:
-- 0,word,4
-- where the last column is the word length.
-- You will also need to create a user with access to this db, which you will add to the 
-- dbconfig.json file used by the word tools app. Example below assumes 'worduser'.
-- DROP DATABASE worddb;
-- CREATE DATABASE worddb;
USE worddb;
CREATE TABLE words(
  word_id INT NOT NULL AUTO_INCREMENT,
  word VARCHAR(60),
  length SMALLINT,
  UNIQUE(word),
  PRIMARY KEY (word_id)
);
ALTER TABLE words ADD UNIQUE word_idx(word);

LOAD DATA INFILE './en.csv' INTO TABLE words
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
GRANT SELECT ON worddb.words TO worduser@localhost;