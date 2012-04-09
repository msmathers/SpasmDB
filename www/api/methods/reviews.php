<?php

include 'base.artist.php';

$query = "SELECT added, title, url, text, thumbnail, album_id FROM reviews WHERE artist_id=" . $ARTIST['id'] . " ORDER BY id DESC LIMIT 20";
$result = mysql_query($query);
$DATA = array();
while ($row = mysql_fetch_assoc($result)) {
    $review = array(
        "added" => $row['added'],
        "title" => $row['title'],
        "url" => $row['url'],
        "text" => $row['text'],
        "thumbnail" => $row['thumbnail']
    );
    if ($row['album_id']) {
        $query = "SELECT name, url, image_small FROM albums WHERE id=" . $row['album_id'];
        $album = mysql_fetch_assoc(mysql_query($query));
        $review['album'] = $album;
    } 
    if (!$row['thumbnail'] && $review['album']) {
        $review['thumbnail'] = $review['album']['image_small'];
    }
    array_push($DATA, $review);
}

?>
