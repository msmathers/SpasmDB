<?php

include 'base.artist.php';

$query = "SELECT title, location, url, date, added FROM shows WHERE artist_id=" . $ARTIST['id'] . " AND date > NOW() ORDER BY date LIMIT 20";
$result = mysql_query($query);
$DATA = array();
while ($row = mysql_fetch_assoc($result)) {
    $show = array(
        "url" => $row['url'],
        "title" => $row['title'],
        "date" => $row['date'],
        "location" => $row['location'],
        "added" => $row['added']
    );
    array_push($DATA, $show);
}

?>
