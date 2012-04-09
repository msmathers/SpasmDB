<?php

include 'base.artist.php';

$query = "SELECT url, title, added, square, thumbnail, medium, large FROM photos WHERE artist_id=" . $ARTIST['id'] . " ORDER BY added DESC LIMIT 20";
$result = mysql_query($query);
$DATA = array();
while ($row = mysql_fetch_assoc($result)) {
    $photos = array(
        "url" => $row['url'],
        "title" => $row['title'],
        "square" => $row['square'],
        "thumbnail" => $row['thumbnail'],
        "medium" => $row['medium'],
        "large" => $row['large'],
        "added" => $row['added']
    );
    array_push($DATA, $photos);
}

?>
