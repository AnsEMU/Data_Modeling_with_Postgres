# Project 1: Data Modeling with Postgres
Startup named **Sparkify** wants to analyze the data that has been grouped on songs and user activity on their new music streaming app.
My first Project in a **Data Engineering** Nanodgree from **Udacity** creates a postgres database `sparkifydb` for analysis of their music app, *Sparkify*.
The aim of the database is to model a data of song and log sets (JSON formated files) with a star schema format.

## Schema design 

The star schema has 1 fact table (songplays), and 4 dimension tables (users, songs, artists, time). DROP, CREATE, INSERT, and SELECT queries are defined in sql_queries.py. create_tables.py uses functions create_database, drop_tables, and create_tables to create the database sparkifydb and the required tables.

Extract, transform, load processes in etl.py populate the songs and artists tables with data derived from the JSON song files, data/song_data. Processed data derived from the JSON log files, data/log_data, is used to populate time and users tables. A SELECT query collects song and artist id from the songs and artists tables and combines this with log file derived data to populate the songplays fact table.

Song play example queries
Simple queries might include number of users with each membership level.

SELECT COUNT(level) FROM users;

Day of the week music most frequently listened to.

SELECT COUNT(weekday) FROM time;

Or, hour of the day music most often listened to.

SELECT COUNT(hour) FROM time;

