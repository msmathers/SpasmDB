<html>
<head>
<link rel="stylesheet" href="css/docs.css" />
</head>
<body>

<div id="header">
<img src="images/logo.gif"/>
<div class="sub">
A simple <a href="http://en.wikipedia.org/wiki/Representational_State_Transfer">REST API</a> for music artist data.  Very beta.
</div>
</div>
</div>


<style>
#toc2 {
	float: left;
	width: 100%;
	background-color: #222;
	margin-bottom: 20px;

}
#toc22 {
	width: 800px;
	margin: 0px auto;
	text-align: left;
}
#toc2 h3 {
	margin: 0px 0px 10px;
	color: #ccc;
}
#toc2 .pod2 {
	float: left;
	background: none;
	padding: 0px 0px 0px 20px;
	margin: 30px 40px;
	border-left: 1px dotted #161616;
}
#toc2 ul {
	padding: 0px;
}
#toc2 ul li {
	font-size: 16px;
	list-style-type: none;
	margin: 0px 0px 5px 0px;
}
</style>


<div id="toc2">
<div id="toc22">

<div class="pod2">
<h3>Artists &raquo;</h3>
<ul>
<li><a href="#">info</a></li>
<li><a href="#">search</a></li>
</ul>
</ul>
</div>

<div class="pod2">
<h3>News &raquo;</h3>
<ul>
<li href="#interviews"><a href="#">interviews</a></li>
<li href="#news"><a href="#">updates</a></li>
<li href="#reviews"><a href="#">reviews</a></li>
<li href="#shows"><a href="#">shows</a></li>
</ul>
</div>


<div class="pod2">
<h3>Media &raquo;</h3>
<ul>
<li href="#audio"><a href="#">audio</a></li>
<li href="#photos"><a href="#">photos</a></li>
<li href="#videos"><a href="#">videos</a></li>
</ul>
</div>


<div class="pod2">
<h3>Statistics &raquo;</h3>
<ul>
<li><a href="#">fans</a></li>
<li><a href="#">listens</a></li>
<li><a href="#">p2p</a></li>
<li><a href="#">videos</a></li>
</ul>
</ul>
</div>

</div>
</div>



<style>
.method {
	width: 800px;
	margin: 0px auto;
	text-align: left;
}
.method h2 {
	color: #ccc;
}
.method p {
	color: #eee;
}
</style>
 
 
<div class="method">


<h2>photos > Returns recently posted artist photos</h2>

<p>
<b>URL:</b> http://spasmdb.com/photos.<i>format</i><br/>
<b>Request Methods:</b> GET<br/>
<b>Response Formats:</b> json, xml
</p>

<h3>Parameters:</h3>
<ul>
<li><b>v</b>: <i>required</i>. API Version</li>
<li><b>artist</b>: <i>required</i>. Artist slug</li>
</ul>

<h3>Sample Request:</h3>
<a href="#">http://spasmdb.com/api/photos.json?v=0.1&artist=meshuggah</a>

<h3>Sample response:</h3>

</div>
<div style="width: 100%; background-color: #000; color: green; text-align: center;">
<div style="text-align: left; width: 800px; margin: 0px auto;">
<pre>
[
  {
    title : "Meshuggah - House of Blues Hollywood - 02/03/09",
    url : "http://www.flickr.com/photos/47466834@N06/4366330293",
    square : "http://farm5.static.flickr.com/4053/4366330293_3b736a0fe7_s.jpg",
    thumbnail : "http://farm5.static.flickr.com/4053/4366330293_3b736a0fe7_t.jpg",
    medium : "http://farm5.static.flickr.com/4053/4366330293_3b736a0fe7_m.jpg",
    large : "http://farm5.static.flickr.com/4053/4366330293_3b736a0fe7_b.jpg",
    added : "Wed Mar 19 07:51:08 +0000 2010"
  }, 
  {
    title : "Meshuggah - House of Blues Hollywood - 02/03/09",
    url : "http://www.flickr.com/photos/47466834@N06/4366330193",
    square : "http://farm5.static.flickr.com/4002/4366330193_1c683bcd7f_s.jpg",
    thumbnail : "http://farm5.static.flickr.com/4002/4366330193_1c683bcd7f_t.jpg",
    medium : "http://farm5.static.flickr.com/4002/4366330193_1c683bcd7f_m.jpg",
    large : "http://farm5.static.flickr.com/4002/4366330193_1c683bcd7f_b.jpg",
    added: "Wed Mar 19 07:51:02 +0000 2010"
  }
]
</pre>
</div>
</div>





</div>







<div id="container">
<div id="container1">

<div id="toc" class="pod">

<h2>Version 0.1</h2>

<ul>
<li href="overview.html"><a href="#">Overview</a></li>
<li href="api_keys.html"><a href="#">API Keys</a></li>
</ul>

<h3>Artist Data</h3>
<ul>
<li href="#audio"><a href="#">audio</a></li>
<li href="#info"><a href="#">info</a></li>
<li href="#interviews"><a href="#">interviews</a></li>
<li href="#news"><a href="#">news</a></li>
<li href="#photos"><a href="#">photos</a></li>
<li href="#reviews"><a href="#">reviews</a></li>
<li href="#shows"><a href="#">shows</a></li>
<li href="#videos"><a href="#">videos</a></li>
</ul>

<h3>Statistics</h3>
<ul>
<li><a href="#">stats/fans</a></li>
<li><a href="#">stats/listens</a></li>
<li><a href="#">stats/p2p</a></li>
<li><a href="#">stats/videos</a></li>
</ul>

<h3>Search</h3>

<ul>
<li><a href="#">search/artists</a></li>
</ul>

</div>



<div id="content" class="pod">

<?php 

$phpfile = "methods/" . $_GET["page"] . ".php";
include $phpfile;

?>

</div>


<div style='clear: both;'></div>
</div>
</div>

<div id='footer'>
Copyright 2009 SpasmDB.<br/>All rights reserved.
</div>

</body>
</html>
