from spasm.web.core import Web
from spasm.web.util import *

import re
import urllib2
import time
from datetime import datetime


class Google(Web):

    INTERVAL = 6.0
    SEARCH_URL = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s&rsz=large&start=%s"
    
    INTERVIEW_QUERY = '"%s" interview'
    REVIEW_QUERY = '"%s" "%s" review'
    
    def search(self, query, validate=True, max_results=32):
        results = []
        for n in range(0,max_results,8):
            url = self.SEARCH_URL % (urllib2.quote(query), n)
            results += self.grabJSON(url, {}).get('responseData',{}).get('results',[])
        if validate:
            for result in results:
                if not self.is_valid(result, query):
                    results.remove(result)
        return results
                    
    def search_reviews(self, artist, album):
        query = self.REVIEW_QUERY % (artist['name'], album['name'])
        results = self.search(query, max_results=8)
        reviews = [{
            'url'      : result['url'],
            'title'     : result['title'],
            'text'      : result['content'],
            'album_id'  : album['id'],
            'album'     : album['name'],
            'artist'    : artist['name'],
            'artist_id' : artist['id']
        } for result in results]
        return reviews
        
    def search_interviews(self, artist):
        query = self.INTERVIEW_QUERY % (artist['name'])
        results = self.search(query, max_results=8)
        interviews = [{
            'url'      : result['url'],
            'title'     : result['title'],
            'text'      : result['content'],
            'artist_id' : artist['id']
        } for result in results]
        return interviews
        
                    
    def is_valid(self, result, query):
        valid_title = True
        valid_content = True
        p = re.compile("['\"](.*?)['\"]", re.I|re.DOTALL|re.M)
        quoted = p.findall(query)
        tokens = p.sub("", query).strip().split(" ")
        for match in quoted + tokens:
            valid_title = valid_title and match.lower() in result['title'].lower()
            valid_content = valid_content and match.lower() in result['content'].lower() 
        valid = valid_title or valid_content
        return valid
        

class Twitter(Web):

    SEARCH_URL = "http://search.twitter.com/search.json?q=%s&rpp=100"
    TWEETS_URL = "http://twitter.com/statuses/user_timeline/%s.json?count=100"
    USER_URL = "http://twitter.com/users/show.json?screen_name=%s"
    
    INTERVAL = 2.0
    REST_INTERVAL = 30.0
    
    def search_tweets(self, query, filter_terms=[]):
        url = self.SEARCH_URL % urllib2.quote(query)
        data = self.grabJSON(url, {}).get('results', [])
        return data
            
    def search_news(self, artist):
        results = self.search_artist_tweets(artist)
        news = self._tweet2news(results, artist, official=True)
        return news
        
    def get_news(self, artist):
        results = self.get_artist_tweets(artist)
        news = self._tweet2news(results, artist, official=True)
        return news
        
    def _tweet2news(self, tweets, artist, official=False):
        username = self._username(artist['twitter_url'])
        news = [{
            'title'     : tweet['text'],
            'url'       : "http://twitter.com/%s/statuses/%s" % (username, tweet['id']),
            'artist_id' : artist['id'],
            'official'  : official
        } for tweet in tweets]
        return news
        
    def get_stats(self, artist):
        _stats = self.get_artist(artist)
        stats = {
            'followers' : _stats.get('followers_count'),
            'friends'   : _stats.get('friends_count'),
            'tweets'    : _stats.get('statuses_count'),
            'artist_id' : artist['id'],
        }
        return [stats]
        
    def search_artist_tweets(self, artist, query="", filter_terms=[]):
        username = self._username(artist['twitter_url'])
        query = "from:%s %s" % (username, query)
        return self.search_tweets(query, filter_terms)
            
    def get_artist(self, artist):
        username = self._username(artist['twitter_url'])
        url = self.USER_URL % urllib2.quote(username)
        data = self.grabJSON(url, {}, interval=self.REST_INTERVAL)
        return data
        
    def get_artist_tweets(self, artist):
        username = self._username(artist['twitter_url'])
        url = self.TWEETS_URL % urllib2.quote(username)
        data = self.grabJSON(url, [], interval=self.REST_INTERVAL)
        return data
        
    def _username(self, url):
        return url.split("/")[-1]
        """
        p = re.compile("http://(?:www\.)?twitter.com/(.*?)(?:/|$)",re.I|re.M)
        m = p.findall(url)
        username = m[0] if m else None
        return username
        """
        
        

class MySpace(Web):

    STATS_REGEX = r'%s\s*</span>.*?Plays:.*?([0-9,]+).*?Views:.*?([0-9,]+).*?Fans:.*?([0-9,]+)'
    STATS_URL = 'http://searchservice.myspace.com/index.cfm?fuseaction=sitesearch.results&qry=%s&type=Music&musictype=2'
    SHOWS_REGEX = re.compile(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2}) (\d{4}).*?(\d:\d+)(A|P).*?<a.*?href="(http://music.myspace.com.*?)".*?>(.*?)</a>.*?<td.*?>(<.*?>)*(.*?)<', re.DOTALL)
    NEWS_REGEX = re.compile(r'<span class="text">(.*?)</span>.*?<a.*?href="(http://blogs.myspace.com.*?)"', re.DOTALL)
    INTERVAL = 5.0

    def get_stats(self, artist):
        '''plays, views, fans'''
        url = self.STATS_URL % urllib2.quote(artist['name'])
        html = self.grabHTML(url)
        artist_url = artist['myspace_url'].replace('http://','')
        artist_url = artist_url.replace(artist['name'].lower(),
            '(<b>)?%s(</b>)?' % artist['name'].lower())
        p = re.compile(self.STATS_REGEX % artist_url, re.DOTALL)
        m = p.findall(html)
        if m:
            stats = [val.replace(',','') for val in m[0]]
            results = dict(zip(['plays','views','fans'], stats[2:5]\
                if len(stats) == 5 else stats[0:3]))
            results['artist_id'] = artist['id']
            return [results]
        else:
            return []

    def get_shows(self, artist):
        html = self.grabHTML(artist['myspace_url'])
        return [{
            'date'      : datetime.strptime('%sM' % ' '.join(show[0:5]), '%b %d %Y %H:%M %p'),
            'url'       : show[5],
            'title'     : show[6],
            'location'  : show[8],
            'artist_id' : artist['id'],
            'official'  : True,
        } for show in self.SHOWS_REGEX.findall(html)]

    def get_news(self, artist):
        html = self.grabHTML(artist['myspace_url'])
        return [{
            'title'     : news[0],
            'url'       : news[1],
            'artist_id' : artist['id'],
            'official'  : True
        } for news in self.NEWS_REGEX.findall(html)]



class BTJunkie(Web):

    DEFAULT_TERMS = ['discography']
    SEARCH_URL = 'http://btjunkie.org/search?q=%s'
    SEARCH_REGEX = re.compile(r'(http://dl.btjunkie.org/.*?torrent)".*?class="BlckUnd">(.*?)</a>.*?(\d+MB).*?\d{2}/\d{2}.*?(?:<font.*?>)+(.*?)</font>.*?(?:<font.*?>)+(.*?)</font>', re.DOTALL)
    INTERVAL = 10.0

    def search_torrents(self, artist, filter_terms=[]):
        url = self.SEARCH_URL % urllib2.quote(artist['name'])
        html = self.grabHTML(url)
        torrents = []
        urls = []
        for torrent in self.SEARCH_REGEX.findall(html):
            title = re.sub('<.*?>','',torrent[1])
            url = torrent[0]
            valid = not bool(filter_terms)
            for term in filter_terms + self.DEFAULT_TERMS:
                if title.lower().count(term.lower()) and url not in urls:
                    valid = True
                    break
            if valid:
                urls.append(url)
                torrents.append({
                    'url'       : url,
                    'title'     : title,
                    'size'      : torrent[2],
                    'seeds'     : torrent[3] if torrent[3] != 'X' else '0',
                    'leechers'  : torrent[4] if torrent[4] != 'X' else '0',
                    'artist_id' : artist['id']
                })
        return torrents



class YouTube(Web):

    SEARCH_URL = 'http://www.youtube.com/results?search_query=%s&page=%s'
    SEARCH_REGEX = re.compile(r'<div class="video-entry">.*?href="(.*?)".*?<img.*?title="(.*?)".*?src="(.*?)".*?class="video-time">.*?(\d+:\d{2}).*?class="video-view-count">([0-9,]+)', re.DOTALL)
    SCRAPE_INTERVAL = 7.5

    JSON_DETAIL_URL = 'http://gdata.youtube.com/feeds/api/videos/%s?alt=json'
    JSON_SEARCH_URL = 'http://gdata.youtube.com/feeds/api/videos?q=%s&v=1&alt=json&start-index=%s'
    JSON_USER_URL = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?alt=json'

    INTERVAL = 5.0
    PAGES = 3
    
    def get_videos(self, artist):
        username = artist['youtube_url'].split("/")[-1]
        url = self.JSON_USER_URL % urllib2.quote(username)
        results = self.grabJSON(url, {}).get('feed', {}).get('entry',[])
        videos = [self._convert_result(result, artist, official=True) for result in results]
        return videos
    
    def search_videos(self, artist, filter_terms=[]):
        videos = []
        artist_name = urllib2.quote(artist['name'])
        for n in [1, 26, 51]:
            url = self.JSON_SEARCH_URL % (artist_name, n)
            results = self.grabJSON(url, {}).get('feed',{}).get('entry',[])
            for result in results:
                valid = not bool(filter_terms)
                title = result.get('title',{}).get('$t')
                for term in filter_terms:
                    if title.lower().count(term.lower()):
                        valid = True
                        break
                if valid:
                    video = self._convert_result(result, artist)
                    videos.append(video)
        return videos
        
    def get_thumbnails(self, video):
        youtube_id = self._youtube_id(video['url'])
        json = self.grabJSON(self.JSON_DETAIL_URL % youtube_id)
        if not json:
            return []
        thumbs = [thumb for thumb in json.get('entry',{}
            ).get('media$group',{}).get('media$thumbnail') if thumb]
        return thumbs
        
    def _convert_result(self, result, artist, official=False):
        title = result.get('title',{}).get('$t')
        views = result.get('yt$statistics',{}).get('viewCount')
        video = {
            'url'       : result.get('link', [{}])[0].get('href'),
            'title'     : title,
            'thumbnail' : result.get('media$group',{}
                ).get('media$thumbnail',[{}])[0].get('url'),
            'duration'  : result.get('media$group',{}
                ).get('yt$duration',{}).get('seconds'),
            'views'     : views if views else 0,
            'artist_id' : artist['id'],
            'official'  : official
        }
        return video
        
    def _youtube_id(self, url):
        p = re.compile("http://(?:www\.)youtube\.com/watch\?v=(.*?)(?:&|/|$)",re.I|re.M)
        m = p.findall(url)
        yid = m[0] if m else None
        return yid
        

class LastFM(Web):

    API_KEY = '8d50b262d08bc4b406b65aabada39907'
    API_SECRET = '9b18cdfa75db57e9fed963f95d07dd26'
    
    ARTIST_URL = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&format=json&artist=%s&api_key=%s'
    TOPALBUMS_URL = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&format=json&artist=%s&api_key=%s'
    TOPTRACKS_URL = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&format=json&artist=%s&api_key=%s'
    TOPTAGS_URL = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&format=json&artist=%s&api_key=%s'
    SIMILAR_URL = 'http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&format=json&artist=%s&api_key=%s'
    
    INTERVAL = 5.0
    
    def get_artist(self, artist):
        url = self.ARTIST_URL % (urllib2.quote(artist['name']), self.API_KEY)
        result = self.grabJSON(url, {}).get('artist')
        if result:
            data = {
                'mbid'         : result['mbid'], 
                'image_small'  : result['image'][0]['#text'] if len(result['image']) > 0 else None,
                'image_medium' : result['image'][1]['#text'] if len(result['image']) > 1 else None,
                'image_large'  : result['image'][2]['#text'] if len(result['image']) > 2 else None,
                'listeners'    : result['stats']['listeners'],
                'playcount'    : result['stats']['playcount'],
                'artist_id'    : artist['id']
            }
            return data
        else:
            return None
        
    def get_top_albums(self, artist):
        url = self.TOPALBUMS_URL % (urllib2.quote(artist['name']), self.API_KEY)
        results = self.grabJSON(url, {}).get('topalbums',{}).get('album', [])
        if isinstance(results, dict): # WTF LastFM?
            results = [results]
        albums = [{
            'name'         : result['name'],
            'url'          : result['url'],
            'playcount'    : result['playcount'],
            'mbid'         : result['mbid'],
            'image_small'  : result['image'][0]['#text'] if len(result['image']) > 0 else None,
            'image_medium' : result['image'][1]['#text'] if len(result['image']) > 1 else None,
            'image_large'  : result['image'][2]['#text'] if len(result['image']) > 2 else None,
            'artist_id'    : artist['id']
        } for result in results]
        return albums
        
    def get_top_tracks(self, artist):
        url = self.TOPTRACKS_URL % (urllib2.quote(artist['name']), self.API_KEY)
        results = self.grabJSON(url, {}).get('toptracks',{}).get('track', [])
        if isinstance(results, dict): # WTF LastFM?
            results = [results]
        tracks = [{
            'name'      : result['name'],
            'url'       : result['url'],
            'listeners' : result['listeners'],
            'mbid'      : result['mbid'],
            'artist_id' : artist['id']
        } for result in results]
        return tracks
        
    def get_top_tags(self, artist):
        '''count, url, name'''
        url = self.TOPTAGS_URL % (urllib2.quote(artist['name']), self.API_KEY)
        results = self.grabJSON(url, {}).get('toptags',{}).get('tag', [])
        if isinstance(results, dict): # WTF LastFM?
            results = [results]
        tags = [{
            'count'     : result['count'],
            'url'       : result['url'],
            'name'      : result['name'],
            'artist_id' : artist['id']
        } for result in results]
        return tags
        
    def get_similar_artists(self, artist):
        url = self.SIMILAR_URL % (urllib2.quote(artist['name']), self.API_KEY)
        results = self.grabJSON(url, {}).get('similarartists',{}).get('artist', [])
        if isinstance(results, dict): # WTF LastFM?
            results = [results]
        artists = [{
            'name'      : result['name'], 
            'url'       : result['url'],
            'mbid'      : result['mbid'], 
            'matchval'  : result['match'],
            'artist_id' : artist['id']
        } for result in results]
        return artists    
        

class Flickr(Web):

    API_KEY = "e6f7bba2ed350cdad2a5e0a1fdd7a6cd"
    API_SECRET_KEY = "93652087da42b7e5"
    SEARCH_URL = "http://api.flickr.com/services/rest/?method=flickr.photos.search&format=json&nojsoncallback=1&api_key=%s"

    INTERVAL = 10.0
    
    def search_photos(self, artist, group_id=None, mode="text"):
        url = self.SEARCH_URL % self.API_KEY
        if group_id:
            url += "&group_id=%s" % group_id
        if mode == "text":
            url += '&text="%s"&sort=relevance' % urllib2.quote(artist['name'])
        else:
            url += "&tags=%s,%s" % (urllib2.quote(artist['name'].replace(" ","")), "concert")
        results = self.grabJSON(url, {}).get('photos',{}).get('photo',[])
        photos = [{
            'title'     : result['title'],
            'url'       : 'http://www.flickr.com/photos/%(owner)s/%(id)s' % result,
            'square'    : 'http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s_s.jpg' % result,
            'thumbnail' : 'http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s_t.jpg' % result,
            'medium'    : 'http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s_m.jpg' % result,
            'large'     : 'http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s_b.jpg' % result,
            'artist_id' : artist['id']
        } for result in results]
        return photos


class TinySong(Web):
    
    SEARCH_URL = "http://tinysong.com/s/%s?limit=32"
    INTERVAL = 10.0

    def search(self, query, filter_terms=[]):
        url = self.SEARCH_URL % urllib2.quote(query)
        results = self.grabCSV(url, [], delimiter=";")
        for result in results:
            if len(result) > 7:
                valid = not bool(filter_terms)
                title = result[2]
                for term in filter_terms:
                    if title.lower().count(term.lower()):
                        valid = True
                        break
                if not valid:
                    results.remove(result)
        return results

    def search_audio(self, artist, validate=True, filter_terms=[]):
        results = self.search(artist['name'], filter_terms=filter_terms)
        if validate:
            for result in results:
                if not result or len(result) < 4 or result[4].lower() != artist['name'].lower():
                    results.remove(result)
        audio = [{
            'url'       : result[7],
            'tiny_url'  : result[0],
            'title'     : result[2],
            'artist_id' : artist['id']
        } for result in results if len(result) > 7]
        return audio

    def search_audio_tracks(self, artist, track, validate=True):
        results = self.search("%s %s" % (artist['name'], track['name']))
        if validate:
            for result in results:
                if not result or len(result) < 4 or result[4].lower() != artist['name'].lower():
                    results.remove(result)
        audio = [{
            'url'       : result[7],
            'tiny_url'  : result[0],
            'title'     : result[2],
            'artist_id' : artist['id']
        } for result in results if len(result) > 7]
        return audio
        
