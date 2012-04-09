<?php

if (!$_GET['artist']) {
    echo "Error: Missing 'artist' parameter";
    exit();
}

$ARTIST_SLUG = mysql_real_escape_string($_GET['artist']);

$result = mysql_query("SELECT id FROM artists WHERE slug='" . $ARTIST_SLUG . "'");
if (mysql_num_rows($result) == 0) {
    echo "Error: Invalid artist slug '" . $ARTIST_SLUG . "'";
    exit();
}

$ARTIST_ID = mysql_result($result,0);

$ARTIST = array("id" => $ARTIST_ID, "slug" => $ARTIST_SLUG);

?>