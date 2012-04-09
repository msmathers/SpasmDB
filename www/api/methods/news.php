<?php

include 'base.artist.php';

$query = "SELECT url, title, added, text, official FROM news WHERE artist_id=" . $ARTIST['id'] . " ORDER BY added DESC LIMIT 20";
$result = mysql_query($query);
$DATA = array();
while ($row = mysql_fetch_assoc($result)) {
    $news = array(
        "url" => $row['url'],
        "title" => $row['title'],
        "text" => $row['text'],
        "official" => ($row['official'] ? true : false),
        "added" => $row['added']
    );
    array_push($DATA, $news);
}

?>
