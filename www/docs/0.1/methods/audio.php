
<h2>audio</h2>
<p>Retrieves links to artist's streamable audio tracks.</p>

<h3>Example:</h3>
<a href="#">http://spasmdb.com/api/audio.json?v=0.1&artist=meshuggah</a>

<h3>Sample response:</h3>
<pre>
[
  {
    title : "Bleed",
    album : "Obzen",
    url : "http://listen.grooveshark.com/song/Bleed/7155311",
    tinyurl : "http://tinysong.com/3L5j"
  }, 
  {
    title : "Rational Gaze",
    album : "Nothing",
    url : "http://listen.grooveshark.com/song/Rational+Gaze/3009245",
    tinyurl : "http://tinysong.com/d8sl"
  }
]
</pre>

<h3>URL:</h3>
<p>http://spasmdb.com/audio.<i>format</i></p>

<h3>Request Methods:</h3>
<p>GET</p>

<h3>Response formats:</h3>
<p>json, xml</p>

<h3>Parameters:</h3>
<ul>
<li><b>v</b>: <i>required</i>. API Version</li>
<li><b>artist</b>: <i>required</i>. Artist slug</li>
</ul>

