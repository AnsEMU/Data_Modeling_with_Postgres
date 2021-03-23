
# Project 1: Data Modeling with Postgres
Startup named **Sparkify** wants to analyze the data that has been grouped on songs and user activity on their new music streaming app.
My first Project in a **Data Engineering** Nanodgree from **Udacity** creates a postgres database `sparkifydb` for analysis of their music app, *Sparkify*.
The aim of the database is to model a data of song and log sets (JSON formated files) with a star schema format.

## Schema design 

The star schema that consists of (Fact & dimentions tables) has 1 fact table which is **songplays**, and 4 dimension tables (users, songs, artists, time).
And in sql_queries.py a drop, create, insert, and select are defined with ON CONFLICT statments, create_tables.py states functions such as create database and tables including drop tables.

![ERD_sparkify](https://user-images.githubusercontent.com/12682524/112122145-a69d9f80-8bc8-11eb-8c8b-51e61ea82895.png)

## ETL Processes (etl.py & etl.ipynb)

Extract, transform, load processes in etl.py generates the songs and artists tables with data obtained from a JSON formatted files, data/song_data. An INSERT querys inserts choosen processed data to song, artist, time, users tables, An attribute from artists and songs tables combined with attributes from log file formed together to populate songplays fact table.

## Project implementation

```
$ python create_tables.py
$ python etl.py
```
## Result tables:

### songplays (Fact Table)

![songplays](https://user-images.githubusercontent.com/12682524/112146889-c5aa2a80-8be4-11eb-894d-b1c94dcc296f.PNG)

### Dimension Tables

#### users table
![users](https://user-images.githubusercontent.com/12682524/112146897-c642c100-8be4-11eb-93aa-41ac65b5d16e.PNG)

#### songs table
![songs](https://user-images.githubusercontent.com/12682524/112146893-c5aa2a80-8be4-11eb-9c42-16299dd6d165.PNG)

#### artists table
![artists](https://user-images.githubusercontent.com/12682524/112146884-c478fd80-8be4-11eb-9991-8f8ed4741bb9.PNG)

#### time table
![time](https://user-images.githubusercontent.com/12682524/112146894-c642c100-8be4-11eb-942d-3522ed42d491.PNG)


### Song_select query:
A query that verifies the selection of a non_null record from songs & artists tables that ware fetched into songplays table:

![songplays 1 row with valid song_id   artist_id](https://user-images.githubusercontent.com/12682524/112146887-c5119400-8be4-11eb-922c-d3b2db9475de.PNG)


## Some table queries:
#### Count the number of Free & Paid users
![Levels of users](https://user-images.githubusercontent.com/12682524/112152404-ef665000-8bea-11eb-83ac-37ff974a368f.PNG)

#### Artists and their location
##### We can see 27 artist with no location specified and 4 each 2 share same location.
![artists and counts of their locations](https://user-images.githubusercontent.com/12682524/112152851-656ab700-8beb-11eb-81b3-02cc6b71c499.PNG)
