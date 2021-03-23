
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
71 files found in data/song_data
1/71 files processed.
2/71 files processed.
3/71 files processed.
4/71 files processed.
5/71 files processed.
6/71 files processed.
7/71 files processed.
8/71 files processed.
9/71 files processed.
10/71 files processed.
11/71 files processed.
12/71 files processed.
13/71 files processed.
14/71 files processed.
15/71 files processed.
16/71 files processed.
17/71 files processed.
18/71 files processed.
19/71 files processed.
20/71 files processed.
21/71 files processed.
22/71 files processed.
23/71 files processed.
24/71 files processed.
25/71 files processed.
26/71 files processed.
27/71 files processed.
28/71 files processed.
29/71 files processed.
30/71 files processed.
31/71 files processed.
32/71 files processed.
33/71 files processed.
34/71 files processed.
35/71 files processed.
36/71 files processed.
37/71 files processed.
38/71 files processed.
39/71 files processed.
40/71 files processed.
41/71 files processed.
42/71 files processed.
43/71 files processed.
44/71 files processed.
45/71 files processed.
46/71 files processed.
47/71 files processed.
48/71 files processed.
49/71 files processed.
50/71 files processed.
51/71 files processed.
52/71 files processed.
53/71 files processed.
54/71 files processed.
55/71 files processed.
56/71 files processed.
57/71 files processed.
58/71 files processed.
59/71 files processed.
60/71 files processed.
61/71 files processed.
62/71 files processed.
63/71 files processed.
64/71 files processed.
65/71 files processed.
66/71 files processed.
67/71 files processed.
68/71 files processed.
69/71 files processed.
70/71 files processed.
71/71 files processed.
30 files found in data/log_data
1/30 files processed.
2/30 files processed.
3/30 files processed.
4/30 files processed.
5/30 files processed.
6/30 files processed.
7/30 files processed.
8/30 files processed.
9/30 files processed.
10/30 files processed.
11/30 files processed.
12/30 files processed.
13/30 files processed.
14/30 files processed.
15/30 files processed.
16/30 files processed.
17/30 files processed.
18/30 files processed.
19/30 files processed.
20/30 files processed.
21/30 files processed.
22/30 files processed.
23/30 files processed.
24/30 files processed.
25/30 files processed.
26/30 files processed.
27/30 files processed.
28/30 files processed.
29/30 files processed.
30/30 files processed.

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
