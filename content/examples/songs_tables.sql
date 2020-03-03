-- SQL commands for creating the tables in the 'songs.db' database.

CREATE TABLE artists
(id INTEGER PRIMARY KEY,
artist TEXT UNIQUE,
country TEXT);

CREATE TABLE albums
(id INTEGER PRIMARY KEY,
album TEXT,
year INTEGER,
artist_id INTEGER,
UNIQUE(album, artist_id),
FOREIGN KEY(artist_id) REFERENCES artists(id));

CREATE TABLE songs
(id INTEGER PRIMARY KEY,
song TEXT,
number INTEGER,
album_id INTEGER,
UNIQUE(number, album_id),
FOREIGN KEY(album_id) REFERENCES albums(id));
