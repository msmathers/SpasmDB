<?php

require 'base.artist.php';

$query = "SELECT added, title, url, album_id FROM audio WHERE artist_id=" . $ARTIST['id'] . " ORDER BY id DESC LIMIT 20";
$result = mysql_query($query);
$DATA = array();
while ($row = mysql_fetch_assoc($result)) {
    $audio = array(
        "added" => $row['added'],
        "title" => $row['title'],
        "url" => $row['url']
    );
    if ($row['album_id']) {
        $query = "SELECT title, url FROM albums WHERE album_id=" . $row['album_id'];
        $album = mysql_fetch_assoc(mysql_query($query));
        $audio['album'] = $album;
    } 
    array_push($DATA, $audio);
}

?>
