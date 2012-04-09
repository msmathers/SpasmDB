<?php

include 'base.artist.php';

$query = "SELECT title, url, duration, thumbnail, views FROM videos WHERE artist_id=" . $ARTIST['id'] . " ORDER BY id DESC LIMIT 20";
$result = mysql_query($query);
$DATA = array();
while ($row = mysql_fetch_assoc($result)) {
    $video = array(
        "url" => $row['url'],
        "title" => $row['title'],
        "duration" => $row['duration'],
        "thumbnail" => $row['thumbnail'],
        "views" => $row['views']
    );
    array_push($DATA, $video);
}

?>
