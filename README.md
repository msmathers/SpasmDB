# SpasmDB - Aggregated music data, served up RESTfully

*Disclaimer: SpasmDB ceased development in 2008. Many of its crawlers likely no longer work. The code has been released purely for reference.*

## Compontents

* Crawlers consume APIs and scrape HTML sources for artist metadata.
* Data is managed through a Python DAO layer with a MySQL backend.
* REST API serves data to clients via HTTP, written in PHP.

## /artists/info

Get artist tags, urls, similar artists, and country of origin.

* URL: /api/artists/info.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
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
```

## /artists/search

Search artist names, find partial matches.

* URL: /api/artists/search.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* query: required. Artist name query

```javascript
[
    {
      slug: "candiria", 
      name: "Candiria"
    },
    {
      slug: "cannibal-corpse", 
      name: "Cannibal Corpse"
    },
    {
      slug: "canvas-solaris", 
      name: "Canvas Solaris"
    }
]
```

## /interviews

Get latest interviews with artist.

* URL: /api/interviews.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
[
  {
    title : "CoC : Meshuggah : Interview",
    text : "With the exception possibly of Opeth, this ironic 
            state of affairs has never been more applicable than 
            in the case of Swedish math-metallers Meshuggah",
    url : "http://www.chroniclesofchaos.com/articles/chats/1-660_meshuggah.aspx",
    added : "2010-03-24 16:51:25"
  }, 
  {
    title : "PyroMusic.net - Interview of: Marten HagstrÅ¡m - Meshuggah",
    text : "Feb 10, 2010 ... We also have: 2 Other Interviews Meshuggah: 
            Interview with Marten HagstrÅ¡m (23/ 08/2008) - 1 Gig Review 
            Meshuggah at the UNSW Roundhouse ...",
    url : "http://www.pyromusic.net/index.php?p=interviews_interview&id=173",
    added : "2010-03-22 12:55:44"
  }
]
```

## /news

Get latest artist updates from myspace, twitter, blogs, etc...

* URL: /api/news.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
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
```

## /reviews

Get latest album reviews for artist.

* URL: /api/reviews.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
[
  {
    "added" :"2010-04-29 04:08:36",
    "title" :"Meshuggah - obZen review - Metal Storm",
    "url" :"http://www.metalstorm.net/pub/review.php%3Freview_id%3D5228",
    "text" :"Meshuggah have not changed their signature style and so " ObZen" stylistically   will have no major surprises for fans of the band. The album is methodically ...",
     "thumbnail":"http://userserve-ak.last.fm/serve/34s/12389183.jpg",
     "album":
       {
        "name":"obZen",
        "url":"http://www.last.fm/music/Meshuggah/obZen",
        "image_small":"http://userserve-ak.last.fm/serve/34s/12389183.jpg"
       }
  },
  {
    "added" : "2010-04-29 02:29:06",
    "title" : "Meshuggah - None [EP] - Metal Storm",
    "url" : "http://www.metalstorm.net/bands/album.php%3Falbum_id%3D1211%26band_id%3D175%26bandname%3DMeshuggah",
    "text" : "Meshuggah - None [EP] ... Ivan, General matters, site programming. Jeff, Reviews  , interviews and events. Thryce, News. Wrathchild, Forums and moderation ...",
    "thumbnail" : "http://images.amazon.com/images/P/B000000H0U.01.MZZZZZZZ.jpg",
    "album": 
      {
        "name" : "None",
        "url" : "http://www.last.fm/music/Meshuggah/None",
        "image_small" : "http://images.amazon.com/images/P/B000000H0U.01.MZZZZZZZ.jpg"
      }
   }
]
```

## /shows

Get artist's upcoming shows information.

* URL: /api/shows.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
[
  {
    url : "http://music.myspace.com/index.cfm?fuseaction=music.showDetails&friendid=5556398&Band_Show_ID=38593159",
    title :"The Bottleneck w/ Converge, Lewd Acts, Black Breath",
    date :"2010-05-10 08:00:00",
    location :"Lawrence, Kansas",
    added :"2010-03-07 10:26:39"
  },
  {
    url :"http://music.myspace.com/index.cfm?fuseaction=music.showDetails&friendid=5556398&Band_Show_ID=38593160",
    title :"Marquis Theater w/ Converge, Lewd Acts, Black Breath",
    date :"2010-05-11 08:00:00",
    location :"Denver, Colorado",
    added :"2010-03-07 10:26:39"
  },
  {
    url : "http://music.myspace.com/index.cfm?fuseaction=music.showDetails&friendid=5556398&Band_Show_ID=38593161",
    title : "Neumos w/ Converge, Lewd Acts, Black Breath",
    date :"2010-05-13 08:00:00",
    location :"Seattle, Washington",
    added :"2010-03-07 10:26:39"
  }
]
```

## /audio

Get artist's latest streamable tracks.

* URL: /api/audio.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
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
```

## /photos

Get latest photos of artist posted on Flickr.

* URL: /api/photos.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
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
```

## /videos

Get latest YouTube videos featuring artist.

* URL: /api/videos.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
[
  {
    url : "http://www.youtube.com/watch?v=eVyH597paQY&feature=youtube_gdata",
    title : "Meshuggah-Obzen",
    duration :"267",
    thumbnail :"http://i.ytimg.com/vi/eVyH597paQY/2.jpg",
    views :"4399"
  }, 
  {
    url : "http://www.youtube.com/watch?v=rtkuhWZ4kA8&feature=youtube_gdata",
    title : "Meshuggah - Future Breed Machine (live)",
    duration : "498",
    thumbnail :"http://i.ytimg.com/vi/rtkuhWZ4kA8/2.jpg",
    views :"876"
  },
  {
    url : "http://www.youtube.com/watch?v=KG8aYATEIQU&feature=youtube_gdata",
    title :"Meshuggah - Spasm",
    duration :"255",
    thumbnail :"http://i.ytimg.com/vi/KG8aYATEIQU/2.jpg",
    views :"16951"
  },
  {
    url :"http://www.youtube.com/watch?v=tW2_QhUMsy4&feature=youtube_gdata",
    title :"meshuggah-spasm",
    duration :"255",
    thumbnail : "http://i.ytimg.com/vi/tW2_QhUMsy4/2.jpg",
    views :"8954"
  }
]
```

## /stats/fans

Get daily MySpace fan totals for artist.

* URL: /api/stats/fans.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
[
  ["2010-01-27" , "452101"],
  ["2010-01-26" , "452078"],
  ["2010-01-25" , "452010"],
  ["2010-01-24" , "451992"]
]
```

## /stats/listens

Get LastFM listen totals for artist.

* URL: /api/stats/listens.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
[
  ["2010-04-07" , "9331194"],
  ["2010-04-06" , "9331194"],
  ["2010-04-05" , "9313532"],
  ["2010-04-04" , "9313532"],
  ["2010-04-03" , "9313532"],
  ["2010-04-02" , "9313271"]
]
```

## /stats/p2p

Get daily peer-to-peer activity around artist.

* URL: /api/stats/p2p.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug
Example »

```javascript
[
  ["2010-04-08" , "1063"],
  ["2010-04-07" , "33"],
  ["2010-04-06" , "4"],
  ["2010-04-05" , "20"],
  ["2010-04-02" , "3"],
  ["2010-03-29" , "2"],
  ["2010-03-26" , "0"],
  ["2010-03-24" , "4"],
  ["2010-03-22" , "1"],
  ["2010-03-10" , "0"]
]
```

## /stats/videos

Get daily YouTube view totals for artist.

* URL: /api/stats/videos.format
* Request Methods: GET
* Response Formats: json, xml

### Parameters

* v: required. API Version
* artist: required. Artist slug

```javascript
[
    ["2010-04-07" , "121784"],
    ["2010-04-06" , "11907"],
    ["2010-04-04" , "29656"],
    ["2010-04-03" , "21213"],
    ["2010-04-02" , "55418"],
    ["2010-04-01" , "23075"],
    ["2010-03-31" , "103569"],
    ["2010-03-29" , "60106"],
    ["2010-03-27" , "235291"],
    ["2010-03-26" , "27692"],
    ["2010-03-25" , "35"],
    ["2010-03-24" , "6475"],
    ["2010-03-23" , "17472"]
]
```

## Authors

Mike Smathers &lt;mikesmathers at gmail dot com&gt;

## License

All code is released under the MIT license. Please read the LICENSE.txt file for more details.