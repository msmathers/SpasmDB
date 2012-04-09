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
    'image_large' : None,
    'ambiguous'   : 0
}

"""
artist = {
    'id'          : 0,
    'name'        : 'Down',
    'slug'        : 'down',
    'myspace_url' : 'http://www.myspace.com/downnola',
    'lastfm_url'  : 'http://www.last.fm/music/Down',
    'twitter_url' : 'http://twitter.com/downnola',
    'youtube_url' : 'http://www.youtube.com/downnolacom',
    'mbid'        : None,
    'image_small' : None,
    'image_medium': None,
    'image_large' : None,
    'ambiguous'   : 1
}
"""

_log("Testing LastFM...")
from spasm.crawlers.lastfm import run as lastfm_run
lastfm_run(artist)

_log("Testing BTJunkie...")
from spasm.crawlers.btjunkie import run as btjunkie_run
btjunkie_run(artist)

_log("Testing Flickr...")
from spasm.crawlers.flickr import run as flickr_run
flickr_run(artist)

_log("Testing Google...")
from spasm.crawlers.google import run as google_run
google_run(artist)

_log("Testing MySpace...")
from spasm.crawlers.myspace import run as myspace_run
myspace_run(artist)

_log("Testing TinySong...")
from spasm.crawlers.tinysong import run as tinysong_run
tinysong_run(artist)

_log("Testing Twitter_REST...")
from spasm.crawlers.twitter_rest import run as twitter_rest_run
twitter_rest_run(artist)

_log("Testing Twitter_Search...")
from spasm.crawlers.twitter_search import run as twitter_search_run
twitter_search_run(artist)

_log("Testing YouTube...")
from spasm.crawlers.youtube import run as youtube_run
youtube_run(artist)


# Done

_log("All done.")
print
