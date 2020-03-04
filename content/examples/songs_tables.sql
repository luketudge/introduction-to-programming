-- SQL commands for creating the tables in the 'songs.db' database.

-- artists:
-- no duplicate artist names
CREATE TABLE artists
(id INTEGER PRIMARY KEY,
artist TEXT UNIQUE,
country TEXT);

-- albums:
-- no duplicate album names for the same artist
-- album artist must exist in the artists table
CREATE TABLE albums
(id INTEGER PRIMARY KEY,
album TEXT,
year INTEGER,
artist_id INTEGER,
UNIQUE(album, artist_id),
FOREIGN KEY(artist_id) REFERENCES artists(id));

-- songs:
-- no duplicate song names for the same album
-- no duplicate song numbers for the same album
-- song album must exist in the albums table
CREATE TABLE songs
(id INTEGER PRIMARY KEY,
song TEXT,
number INTEGER,
album_id INTEGER,
UNIQUE(song, album_id),
UNIQUE(number, album_id),
FOREIGN KEY(album_id) REFERENCES albums(id));
