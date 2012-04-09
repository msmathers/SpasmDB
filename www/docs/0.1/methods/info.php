
<h2>info</h2>
<p>Retrieves various artist information including urls, tags, similar artists, etc...</p>

<h3>Example:</h3>
<a href="#">http://spasmdb.com/api/info.json?v=0.1&artist=meshuggah</a>

<h3>Sample response:</h3>
<pre>
{
    name : "Meshuggah",
    slug : "meshuggah",
    country : "se",
    tags : ["progressive", "metal", "math"],
    similar : [
        {name : "Frederik Thordendals", url : "http://lastfm.com/meshuggah"}
        {name : "Strapping Young Lad", url : "http://lastfm.com/syl"}
    ],
    urls : {
        lastfm : 'http://www.lastfm.com/meshuggah',
        youtube : 'http://www.youtube.com/users/meshuggah',
        twitter : 'http://www.twitter.com/meshuggahband',
        myspace : 'http://myspace.com/meshuggah'
    }
}
</pre>

<h3>URL:</h3>
<p>http://spasmdb.com/info.<i>format</i></p>

<h3>Request Methods:</h3>
<p>GET</p>

<h3>Response formats:</h3>
<p>json, xml</p>

<h3>Parameters:</h3>
<ul>
<li><b>v</b>: <i>required</i>. API Version</li>
<li><b>artist</b>: <i>required</i>. Artist slug</li>
</ul>

<h3>Notes:</h3>
<ul>
<li>Method may return similar artists that aren't in our system.</li>
</ul>

