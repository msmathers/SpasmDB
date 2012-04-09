from spasm.data.config import CONFIG

print """
    WARNING: This is a test script, do NOT run on production!

    Test data will be inserted into the following database:

    Host: "%(host)s"
    Name: "%(db)s"

    Abort this script with Ctrl+C, proceeding in 10 seconds...
""" % CONFIG

import time
time.sleep(10)

from spasm.web import sources as _web
from spasm.data import sources as _data

def _log(msg):
    print
    print "(%s) %s" % (time.ctime(), msg)

artist = {
    'id'          : 0,
    'name'        : 'Meshuggah',
    'slug'        : 'meshuggah',
    'myspace_url' : 'http://www.myspace.com/meshuggah',
    'lastfm_url'  : 'http://www.last.fm/music/Meshuggah',
    'twitter_url' : 'http://twitter.com/meshuggahband',
    'youtube_url' : 'http://www.youtube.com/user/Meshuggah',
    'mbid'        : None,
    'image_small' : None,
    'image_medium': None,
    'image_large' : None
}
   

# LastFM

_log("Testing LastFM()...")
web = _web.LastFM()
data = _data.LastFM()

_log("LastFM.get_artist(<%s>)..." % artist['name'])
_artist = web.get_artist(artist)

for field in _artist:
    if field in artist:
        artist[field] = _artist[field]

data.update_artist(artist)
data.add_stats({
    'artist_id' : artist['id'],
    'listeners' : _artist['listeners'],
    'playcount' : _artist['playcount']
})
    
_log("LastFM.get_top_albums(<%s>)..." % artist['name'])
albums = web.get_top_albums(artist)
for album in albums:
    data.update_album(album)

_log("LastFM.get_top_tracks(<%s>)..." % artist['name'])
tracks = web.get_top_tracks(artist)
for track in tracks:
    data.update_track(track)

_log("LastFM.get_top_tags(<%s>)..." % artist['name'])
tags = web.get_top_tags(artist)
for tag in tags:
    data.update_tag(tag)

_log("LastFM.get_similar_artists(<%s>)..." % artist['name'])
similar = web.get_similar_artists(artist)
for s in similar:
    data.update_similar(s)

 
# Google

_log("Testing Google()...")
web = _web.Google()
data = _data.Google()

_log("Google.search_reviews(<%s>)" % artist['name'])
album = {'name': "Catch 33", 'id': 0}
reviews = web.search_reviews(artist, album)
for review in reviews:
    data.update_review(review)

_log("Google.search_interviews(<%s>)" % artist['name'])
interviews = web.search_interviews(artist)
for interview in interviews:
    data.update_interview(interview)


# Twitter

_log("Testing Twitter()...")
web = _web.Twitter()
data = _data.Twitter()

_log("Twitter.search_news(<%s>)..." % artist['name'])
news = web.search_news(artist)
for n in news:
    data.update_news(n)

_log("Twitter.get_news(<%s>)..." % artist['name'])
news = web.get_news(artist)
for n in news:
    data.update_news(n)

_log("Twitter.get_stats(<%s>)..." % artist['name'])
stats = web.get_stats(artist)
if stats:
    data.add_stats(stats[0])


# Myspace

_log("Testing MySpace()...")
web = _web.MySpace()
data = _data.MySpace()

_log("MySpace.get_stats(<%s>)..." % artist['name'])
stats = web.get_stats(artist)
if stats:
    data.add_stats(stats[0])

_log("MySpace.get_news(<%s>)..." % artist['name'])
news = web.get_news(artist)
for n in news:
    data.update_news(n)

_log("MySpace.get_shows(<%s>)..." % artist['name'])
shows = web.get_shows(artist)
for show in shows:
    data.update_show(show)


# BTJunkie

_log("Testing BTJunkie()...")
web = _web.BTJunkie()
data = _data.BTJunkie()

_log("BTJunkie.search_torrents(<%s>)..." %  artist['name'])
torrents = web.search_torrents(artist)
for torrent in torrents:
    data.update_torrent(torrent)


# YouTube

_log("Testing YouTube()...")
web = _web.YouTube()
data = _data.YouTube()

_log("YouTube.get_videos(<%s>)..." % artist['name'])
videos = web.get_videos(artist)
for video in videos:
    data.update_video(video)

_log("YouTube.search_videos(<%s>)..." % artist['name'])
videos = web.search_videos(artist)
for video in videos:
    data.update_video(video)


# Flickr

_log("Testing Flickr()...")
web = _web.Flickr()
data = _data.Flickr()

_log("Flickr.search_photos(<%s>)..." % artist['name'])
photos = web.search_photos(artist)
for photo in photos:
    data.update_photo(photo)


# TinySong

_log("Testing TinySong()...")
web = _web.TinySong()
data = _data.TinySong()

_log("TinySong.search_audio(<%s>)..." % artist['name'])
audio = web.search_audio(artist)
for song in audio:
    data.update_audio(song)


# Done

_log("All done.")
print
