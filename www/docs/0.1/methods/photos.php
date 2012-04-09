
<h2>photos</h2>
<p>Returns recently posted artist photos</p>

<h3>Example:</h3>
<a href="#">http://spasmdb.com/api/photos.json?v=0.1&artist=meshuggah</a>

<h3>Sample response:</h3>
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

<h3>URL:</h3>
<p>http://spasmdb.com/photos.<i>format</i></p>

<h3>Request Methods:</h3>
<p>GET</p>

<h3>Response formats:</h3>
<p>json, xml</p>

<h3>Parameters:</h3>
<ul>
<li><b>v</b>: <i>required</i>. API Version</li>
<li><b>artist</b>: <i>required</i>. Artist slug</li>
</ul>

