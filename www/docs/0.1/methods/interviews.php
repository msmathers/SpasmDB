
<h2>interviews</h2>
<p>Returns links to recently posted artist interviews.</p>

<h3>Example:</h3>
<a href="#">http://spasmdb.com/api/interviews.json?v=0.1&artist=meshuggah</a>

<h3>Sample response:</h3>
<pre>
[
  {
    title : "CoC : Meshuggah : Interview",
    text : "With the exception possibly of Opeth, this ironic 
            state of affairs has never been more applicable than 
            in the case of Swedish math-metallers Meshuggah",
    url : "http://www.chroniclesofchaos.com/articles/chats/1-660_meshuggah.aspx",
    added : "Wed Mar 24 16:51:25 +0000 2010"
  }, 
  {
    title : "PyroMusic.net - Interview of: Marten Hagstršm - Meshuggah",
    text : "Feb 10, 2010 ... We also have: 2 Other Interviews Meshuggah: 
            Interview with Marten Hagstršm (23/ 08/2008) - 1 Gig Review 
            Meshuggah at the UNSW Roundhouse ...",
    url : "http://www.pyromusic.net/index.php?p=interviews_interview&id=173",
    added : "Mon Feb 12 13:22:10 +0000 2010"
  }
]
</pre>

<h3>URL:</h3>
<p>http://spasmdb.com/interviews.<i>format</i></p>

<h3>Request Methods:</h3>
<p>GET</p>

<h3>Response formats:</h3>
<p>json, xml</p>

<h3>Parameters:</h3>
<ul>
<li><b>v</b>: <i>required</i>. API Version</li>
<li><b>artist</b>: <i>required</i>. Artist slug</li>
</ul>

