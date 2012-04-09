<?php

require 'base.artist.php';

$query = "SELECT DATE_FORMAT(date, '%Y-%m-%d') as dateval, MAX(fans) as fans FROM myspace_stats WHERE artist_id=".$ARTIST['id']." GROUP BY dateval ORDER BY dateval DESC LIMIT 14";
$results = mysql_query($query);

// Generate daily stats

$DATA = array();
while ($row = mysql_fetch_row($results)) {
    array_push($DATA, $row);
}

?>