FROM mysql/mysql-server
COPY createdb.sql gen_word_data.sh line2csv.py .
RUN python3 gen_word_data.sh