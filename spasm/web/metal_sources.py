from spyder.web.core import Web
from spyder.web.util import *

import re
import urllib2
import time

class Blabbermouth(Web):

    INTERVAL = 5.0
    URL_PREFIX = 'http://www.roadrunnerrecords.com/blabbermouth.net/'
    NEWS_URL = 'http://feeds.feedburner.com/blabbermouth'
    REVIEWS_URL = 'http://www.roadrunnerrecords.com/blabbermouth.net/reviews.aspx'
    REVIEWS_REGEX = re.compile(r'class="cdReviews">(<.*?>)*(.*?)(<.*?>)*"(.*?)".*?<a.*?href="(.*?)".*?<img.*?src="(.*?)"',re.DOTALL)


    def get_latest_news(self):
        '''description, title, link, guid'''
        dom = self.grabXML(self.NEWS_URL, conf=(2,1))
        news = self.grabItems(dom)
        return news

    def get_latest_reviews(self):
        '''artist, album, link, thumbnail'''
        html = self.grabHTML(self.REVIEWS_URL)
        return [{
            'artist'   : review[1].title().strip(),
            'album'    : review[3].strip(),
            'link'     : '%s%s' % (self.URL_PREFIX, review[4]),
            'thumbnail': '%s%s' % (self.URL_PREFIX, review[5])
        } for review in self.REVIEWS_REGEX.findall(html)]


class MetalArchives(Web):

    INTERVAL = 5.0
    URL_PREFIX = 'http://www.metal-archives.com/'
    REVIEWS_URL = 'http://www.metal-archives.com/reviews.php'
    REVIEWS_REGEX = re.compile(r'<td width=\'35%\'>.*?<b>(.*?) - (.*?)</b>.*?<a.*?href=\'(.*?)\'.*?(\d{1,3}%)',re.DOTALL)

    def get_latest_reviews(self):
        '''artist, album, link, rating'''
        html = self.grabHTML(self.REVIEWS_URL)
        return [{
            'artist' : re.sub('\s\(.*?\)','',review[0]),
            'album'  : review[1],
            'link'   : '%s%s' % (self.URL_PREFIX, review[2]),
            'rating' : review[3]
        } for review in self.REVIEWS_REGEX.findall(html)]


class MetalReview(Web):

    INTERVAL = 5.0
    REVIEWS_URL = 'http://metalreview.com/RSS/LatestReviewsRss.ashx'

    def get_latest_reviews(self):
        '''artist, album, link, description'''
        dom = self.grabXML(self.REVIEWS_URL)
        reviews = self.grabItems(dom)
        return [{
            'artist': review['title'].split('-')[0].strip(),
            'album' : review['title'].split('-')[1].strip(),
            'link'  : review['link']
        } for review in reviews]


class Lambgoat(Web):

    INTERVAL = 5.0
    NEWS_URL = 'http://www.lambgoat.com/rss/news/'
    REVIEWS_URL = 'http://lambgoat.com/reviews/'
    URL_PREFIX = 'http://www.lambgoat.com/'
    REVIEWS_REGEX = re.compile(r'<td.*?width="33%".*?<img.*?src="(.*?)".*?width="60".*?<span.*?>(.*?)</span>.*?<a.*?href="(.*?)".*?>(.*?)</a>',re.DOTALL)

    def get_latest_news(self):
        '''description, title, link, guid'''
        dom = self.grabXML(self.NEWS_URL, conf=(0,0))
        news = self.grabItems(dom)
        return news

    def get_latest_reviews(self):
        '''artist, album, link, thumbnail'''
        html = self.grabHTML(self.REVIEWS_URL)
        return [{
            'artist'   : review[1].title().strip(),
            'album'    : review[3].strip(),
            'link'     : '%s%s' % (self.URL_PREFIX, review[2]),
            'thumbnail': '%s%s' % (self.URL_PREFIX, review[0])
        } for review in self.REVIEWS_REGEX.findall(html)]

