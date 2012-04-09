
<h2>news</h2>
<p>Returns links to latest artist news from myspace, twitter, blogs, etc...</p>

<h3>Example:</h3>
<a href="#">http://spasmdb.com/api/news.json?v=0.1&artist=meshuggah</a>

<h3>Sample response:</h3>
<pre>
[
  {
    title : "MESHUGGAH Featured in Iron Man 2 Video Game!",
    text : "",
    url : "http://blogs.myspace.com/index.cfm?fuseaction=blog.view
           &friendId=9813014&blogId=533175358",
    added : "Wed Apr 29 02:04:25 +0000 2010"
  }, 
  {
    title : "Alive DVD review in May issue of Premier Guitar",
    text : "Alive DVD review in May issue of Premier Guitar",
    url : "http://twitter.com/Meshuggahband/statuses/12659939898",
    added : "Mon Apr 29 13:34:10 +0000 2010"
  }
]
</pre>

<h3>URL:</h3>
<p>http://spasmdb.com/news.<i>format</i></p>

<h3>Request Methods:</h3>
<p>GET</p>

<h3>Response formats:</h3>
<p>json, xml</p>

<h3>Parameters:</h3>
<ul>
<li><b>v</b>: <i>required</i>. API Version</li>
<li><b>artist</b>: <i>required</i>. Artist slug</li>
</ul>

