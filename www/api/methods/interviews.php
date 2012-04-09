<?php

require 'base.artist.php';

$query = "SELECT url, title, added, text FROM interviews WHERE artist_id=" . $ARTIST['id'] . " ORDER BY added DESC LIMIT 20";
$result = mysql_query($query);
$DATA = array();
while ($row = mysql_fetch_assoc($result)) {
    $interview = array(
        "url" => $row['url'],
        "title" => $row['title'],
        "text" => $row['text'],
        "added" => $row['added']
    );
    array_push($DATA, $interview);
}

?>
