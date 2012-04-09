from spasm.web.sources import *
import time

def _log(msg):
    print
    print "(%s) %s" % (time.ctime(), msg)

def _print(results):
    for i, result in enumerate(results):
        print i, result
    print

artist = {
    'id'   : 0,
    'name'        : 'Meshuggah',
    'slug'        : 'meshuggah',
    'myspace_url' : 'http://www.myspace.com/meshuggah',
    'lastfm_url'  : 'http://www.last.fm/music/Meshuggah',
    'twitter_url' : 'http://twitter.com/meshuggahband',
    'youtube_url' : 'http://www.youtube.com/user/Meshuggah'
}
    
# Google

_log("Testing Google()...")
google = Google()

query = '"%s"' % artist['name']
_log("Google.search(%s)" % query)
results = google.search(query)
_print(results)

_log("Google.search_reviews(<%s>)" % artist['name'])
album = {'name': "Catch 33", 'id': 0}
reviews = google.search_reviews(artist, album)
_print(reviews)

_log("Google.search_interviews(<%s>)" % artist['name'])
interviews = google.search_interviews(artist)
_print(interviews)


# Twitter

_log("Testing Twitter()...")
twitter = Twitter()

query = '"%s"' % artist['name']
_log("Twitter.search_tweets(%s)..." % query)
tweets = twitter.search_tweets(query)
_print(tweets)

_log("Twitter.search_news(<%s>)..." % artist['name'])
news = twitter.search_news(artist)
_print(news)

_log("Twitter.get_news(<%s>)..." % artist['name'])
news = twitter.get_news(artist)
_print(news)

_log("Twitter.get_artist(<%s>)..." % artist['name'])
_artist = twitter.get_artist(artist)
print _artist if _artist else "No results."


# Myspace

_log("Testing MySpace()...")
myspace = MySpace()

_log("MySpace.get_stats(<%s>)..." % artist['name'])
stats = myspace.get_stats(artist)
print stats[0] if stats else "No stats."

_log("MySpace.get_news(<%s>)..." % artist['name'])
news = myspace.get_news(artist)
print news[0] if news else "No news."

_log("MySpace.get_shows(<%s>)..." % artist['name'])
shows = myspace.get_shows(artist)
print shows[0] if shows else "No shows."


# BTJunkie

_log("Testing BTJunkie()...")
btjunkie = BTJunkie()

_log("BTJunkie.search_torrents(<%s>)..." %  artist['name'])
torrents = btjunkie.search_torrents(artist)
_print(torrents)


# YouTube

_log("Testing YouTube()...")
youtube = YouTube()

_log("YouTube.get_videos(<%s>)..." % artist['name'])
videos = youtube.get_videos(artist)
_print(videos)

_log("YouTube.search_videos(<%s>)..." % artist['name'])
videos = youtube.search_videos(artist)
_print(videos)

if videos:
    _log("YouTube.get_thumbnails(<%s>)..." % artist['name'])
    thumbs = youtube.get_thumbnails(videos[0])
    print thumbs[0] if thumbs else "No thumbs."
else:
    print "Warning: Could not test YouTube.get_thumbnails(), no videos available..."
print


# LastFM

_log("Testing LastFM()...")
lastfm = LastFM()

_log("LastFM.get_artist(<%s>)..." % artist['name'])
_artist = lastfm.get_artist(artist)
print _artist if _artist else "No results."

_log("LastFM.get_top_albums(<%s>)..." % artist['name'])
albums = lastfm.get_top_albums(artist)
_print(albums)

_log("LastFM.get_top_tracks(<%s>)..." % artist['name'])
tracks = lastfm.get_top_tracks(artist)
_print(tracks)

_log("LastFM.get_top_tags(<%s>)..." % artist['name'])
tags = lastfm.get_top_tags(artist)
_print(tags)

_log("LastFM.get_similar_artists(<%s>)..." % artist['name'])
similar = lastfm.get_similar_artists(artist)
_print(similar)


# Flickr

_log("Testing Flickr()...")
flickr = Flickr()

_log("Flickr.search_photos(<%s>)..." % artist['name'])
photos = flickr.search_photos(artist)
_print(photos)


# TinySong

_log("Testing TinySong()...")
tinysong = TinySong()

_log("TinySong.search_audio(<%s>)..." % artist['name'])
audio = tinysong.search_audio(artist)
_print(audio)


# Done

_log("All done.")
print
