<?php

// Check for query
$QUERY = $_GET['query'];
if (!$QUERY) {
	echo "Error: Missing query parameter";
	exit();
}
$QUERY = mysql_real_escape_string($QUERY);

$query = "SELECT slug, name FROM artists WHERE name LIKE '%" . $QUERY . "%' ORDER BY name LIMIT 50";
$result = mysql_query($query);
$DATA = array();
while ($row = mysql_fetch_assoc($result)) {
    $artist = array(
        "slug" => $row['slug'],
        "name" => $row['name'],
    );
    array_push($DATA, $artist);
}

?>
