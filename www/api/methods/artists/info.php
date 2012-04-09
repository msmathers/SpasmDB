<?php

require 'base.artist.php';

$query = "SELECT name, slug, country FROM artists WHERE slug='" . $ARTIST['slug'] . "'";
$result = mysql_query($query);
$DATA = mysql_fetch_assoc($result);

$DATA['similar'] = array();
$query = "SELECT name, url FROM similar WHERE artist_id=" . $ARTIST['id'] . " ORDER BY matchval DESC LIMIT 5";
$result = mysql_query($query);
while ($row = mysql_fetch_assoc($result)) {
    array_push($DATA['similar'], $row);
}

$DATA['tags'] = array();
$query = "SELECT name, url FROM tags WHERE artist_id=" . $ARTIST['id'] . " ORDER BY count DESC LIMIT 5";
$result = mysql_query($query);
while ($row = mysql_fetch_assoc($result)) {
    array_push($DATA['tags'], $row);
}

$query = "SELECT lastfm_url as lastfm, myspace_url as myspace, youtube_url as youtube, twitter_url as twitter, facebook_url as facebook FROM artists WHERE id=" . $ARTIST['id'];
$result = mysql_query($query);
$DATA['links'] = mysql_fetch_assoc($result);

?>
