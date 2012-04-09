<?php

/*
// API Key hack
$API_KEY = $_GET['api_key'];
if(!$API_KEY || $API_KEY != "dmtlsdmdma") {
    exit();
}*/

$conn = mysql_connect('localhost','spasmdb','5vhagguhsem');
mysql_select_db('spasm',$conn);


// 0. Config

$CURRENT_VERSION = "0.1";
$API_PATH = "/opt/spasmdb/www/api/";


// 1. Verify params

$FORMAT = $_GET['format'];
$METHOD = trim($_GET['method'], "/");
$VERSION = ($_GET['version'] ? $_GET['version'] : $CURRENT_VERSION);


// 2. Generate data

$method_path = $API_PATH . "methods/" . $METHOD . ".php";
if (file_exists($method_path)) {
    include $method_path;
} else {
    echo "Error: Method '" . $METHOD . "' does not exist";
}


// 3. Render to output format

$format_path = $API_PATH . "formats/" . $FORMAT . "/" . $METHOD . ".php";
if (file_exists($format_path)) {
    include $format_path;
} else if ($FORMAT == "json") {
    $json = json_encode($DATA);
    echo $json;
} else {
    echo "Error: '" . $FORMAT . "' output unavailable for method '" . $METHOD . "'";
}

?>
