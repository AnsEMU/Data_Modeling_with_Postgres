# DROP TABLES

songplay_table_drop = """DROP table if exists songplays;"""
user_table_drop = """DROP table if exists users"""
song_table_drop = """DROP table if exists songs"""
artist_table_drop = """DROP table if exists artists"""
time_table_drop = """DROP table if exists time"""

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (
    songplay_id serial NOT NULL PRIMARY KEY,
    start_time bigint NOT NULL,
    userId int NOT NULL,
    level varchar NOT NULL,
    song_id varchar,
    artist_id varchar,
    sessionId int NOT NULL,
    location varchar,
    userAgent varchar
);
""")
user_table_create = ("""
  CREATE TABLE IF NOT EXISTS users (
  userId int PRIMARY KEY,
  firstName varchar,
  lastName varchar,
  gender varchar,
  level varchar
  );
""")

song_table_create = ("""
  CREATE TABLE IF NOT EXISTS songs (
  song_id varchar PRIMARY KEY,
  title varchar,
  artist_id varchar,
  year int,
  duration float
  );
  """)

artist_table_create = ("""
  CREATE TABLE IF NOT EXISTS artists (
  artist_id varchar PRIMARY KEY,
  artist_name varchar not null,
  artist_location varchar,
  artist_latitude numeric,
  artist_longitude numeric
  );
  """)

time_table_create = ("""
  CREATE TABLE IF NOT EXISTS time (
  start_time BIGINT PRIMARY KEY,
  hour int,
  day int,
  week int,
  month int,
  year int,
  weekday int
  );
  """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays  
   (start_time, userId, level, song_id, artist_id, sessionId, location, userAgent) 
   VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
   ON CONFLICT DO NOTHING;""")

user_table_insert = ("""
  INSERT INTO users 
  (userId ,firstName ,lastName ,gender , level) 
  VALUES (%s, %s, %s, %s, %s) 
  ON CONFLICT (userId) DO UPDATE SET level = excluded.level;""")

song_table_insert = ("""
  INSERT INTO songs 
  (song_id ,title ,artist_id ,year ,duration) 
  VALUES (%s, %s, %s, %s, %s) 
  ON CONFLICT (song_id) DO NOTHING;""")

artist_table_insert = ("""
  INSERT INTO artists 
  (artist_id ,artist_name ,artist_location ,artist_latitude ,artist_longitude) 
  VALUES (%s, %s, %s, %s, %s) 
  ON CONFLICT (artist_id) DO NOTHING;""")

time_table_insert = ("""
  INSERT INTO time 
  (start_time ,hour ,day ,week ,month ,year ,weekday) 
  VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING;""")

# FIND SONGS

song_select = ("""select s.song_id, a.artist_id
  from songs s
  join artists a
  on s.artist_id=a.artist_id
  where s.title=%s and a.artist_name=%s and s.duration=%s
  GROUP BY
  1,2;
""")
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
