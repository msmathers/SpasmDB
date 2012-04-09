<?php

require 'base.artist.php';

$query = "SELECT DATE_FORMAT(datev, '%Y-%m-%d') as dateval, SUM(seeds) FROM (SELECT id, max(date) as datev, torrent_id, seeds FROM torrent_stats WHERE artist_id=".$ARTIST['id']." GROUP BY torrent_id) as stats GROUP BY dateval ORDER BY dateval DESC LIMIT 14";
$results = mysql_query($query);

// Generate daily stats

$DATA = array();
while ($row = mysql_fetch_row($results)) {
    array_push($DATA, $row);
}

?>