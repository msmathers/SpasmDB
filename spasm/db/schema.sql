CREATE TABLE audio (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(255) NOT NULL UNIQUE,
    tiny_url VARCHAR(255) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    album VARCHAR(255),
    track_id INT(11),
    album_id INT(11),

    artist_id INT(11) NOT NULL,
    valid TINYINT(1) NOT NULL DEFAULT 1,

    PRIMARY KEY id (id)
);

CREATE TABLE artists (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(128) NOT NULL,
    slug VARCHAR(128) NOT NULL UNIQUE,
    country VARCHAR(2),
    mbid VARCHAR(40),
    lastfm_url VARCHAR(255),
    myspace_url VARCHAR(255),
    youtube_url VARCHAR(255),
    twitter_url VARCHAR(255),
    facebook_url VARCHAR(255),
    website_url VARCHAR(255),
    image_small VARCHAR(255),
    image_medium VARCHAR(255),
    image_large VARCHAR(255),
    ambiguous TINYINT(1) NOT NULL DEFAULT 0,

    PRIMARY KEY id (id)
);

CREATE TABLE albums (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(128) NOT NULL,
    url VARCHAR(255) NOT NULL UNIQUE,
    playcount INT(11),
    mbid VARCHAR(40),
    image_small VARCHAR(255),
    image_medium VARCHAR(255),
    image_large VARCHAR(255),
    artist_id INT(11) NOT NULL,

    PRIMARY KEY id (id)
);

CREATE TABLE interviews (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(255) NOT NULL UNIQUE,
    title VARCHAR(255),
    text TEXT,
    thumbnail VARCHAR(255),

    artist_id INT(11) NOT NULL,
    valid TINYINT(1) NOT NULL DEFAULT 1,

    PRIMARY KEY id (id)
);

CREATE TABLE lastfm_stats (
    id INT(11) NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    listeners INT(11),
    playcount INT(11),
    artist_id INT(11) NOT NULL,

    PRIMARY KEY id (id)
);

CREATE TABLE myspace_stats (
    id INT(11) NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    plays INT(11),
    views INT(11),
    fans INT(11),
    artist_id INT(11) NOT NULL,

    PRIMARY KEY id (id)
);

CREATE TABLE news (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(255) NOT NULL UNIQUE,
    title VARCHAR(255),
    text TEXT,

    artist_id INT(11) NOT NULL,
    valid TINYINT(1) NOT NULL DEFAULT 1,
    official TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY id (id)   
);

CREATE TABLE photos (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(255) NOT NULL UNIQUE,
    title VARCHAR(255),
    square VARCHAR(255),
    thumbnail VARCHAR(255),
    medium VARCHAR(255),
    large VARCHAR(255),

    artist_id INT(11) NOT NULL,
    valid TINYINT(1) NOT NULL DEFAULT 1,

    PRIMARY KEY id (id)   
);

CREATE TABLE reviews (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(255) NOT NULL UNIQUE,
    title VARCHAR(255),
    text TEXT,
    thumbnail VARCHAR(255),
    album_id INT(11),
    artist VARCHAR(255),
    album VARCHAR(255),
    rating VARCHAR(15),

    artist_id INT(11) NOT NULL,
    valid TINYINT(1) NOT NULL DEFAULT 1,

    PRIMARY KEY id (id)   
);

CREATE TABLE shows (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date TIMESTAMP NOT NULL,
    url VARCHAR(255) NOT NULL UNIQUE,
    title VARCHAR(255),
    location VARCHAR(255),

    artist_id INT(11) NOT NULL,
    valid TINYINT(1) NOT NULL DEFAULT 1,
    official TINYINT(1) NOT NULL DEFAULT 0,

    PRIMARY KEY id (id) 
);

CREATE TABLE similar (
    id INT(11) NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    mbid VARCHAR(40),
    matchval INT(11),  
    artist_id INT(11) NOT NULL,

    PRIMARY KEY id (id)  
);

CREATE TABLE tags (
    id INT(11) NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    count INT(11),  
    artist_id INT(11) NOT NULL,

    PRIMARY KEY id (id)  
);

CREATE TABLE torrent_stats (
    id INT(11) NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    torrent_id INT(11) NOT NULL,
    leechers INT(11),
    seeds INT(11),
    artist_id INT(11) NOT NULL,
 
    PRIMARY KEY id (id)
);

CREATE TABLE torrents ( 
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    url VARCHAR(255) NOT NULL UNIQUE,
    title VARCHAR(255) NOT NULL,
    size VARCHAR(20),
    leechers INT(11),
    seeds INT(11),

    artist_id INT(11) NOT NULL,
    valid TINYINT(1) NOT NULL DEFAULT 1,

    PRIMARY KEY id (id)
);

CREATE TABLE tracks (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(255) NOT NULL,   
    url VARCHAR(255) NOT NULL UNIQUE,
    listeners INT(11),
    mbid VARCHAR(40),
    artist_id INT(11) NOT NULL,

    PRIMARY KEY id (id)
);

CREATE TABLE twitter_stats (
    id INT(11) NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    followers INT(11),
    friends INT(11),
    tweets INT(11),
    artist_id INT(11) NOT NULL,

    PRIMARY KEY id (id)   
);

CREATE TABLE videos (
    id INT(11) NOT NULL AUTO_INCREMENT,
    added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(255) NOT NULL,   
    url VARCHAR(255) NOT NULL UNIQUE,
    duration VARCHAR(20),
    views INT(11),
    thumbnail VARCHAR(255),

    artist_id INT(11) NOT NULL,
    valid TINYINT(1) NOT NULL DEFAULT 1,
    official TINYINT(1) NOT NULL DEFAULT 0,

    PRIMARY KEY id (id)  
);

CREATE TABLE youtube_stats (
    id INT(11) NOT NULL AUTO_INCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    video_id INT(11) NOT NULL,
    views INT(11),
    artist_id INT(11) NOT NULL,

    PRIMARY KEY id (id)
);

