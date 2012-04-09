from spyder.data.core import Data
from spyder.data.util import *

import time

class Blabbermouth(Data):

    def update_news(self, newNews):
        matches = """
            artist_id='%s' AND link='%s'
        """ % (newNews['artist_id'], escape(newNews['link']))
        return self._update(newNews, 'news', matches)

    def update_review(self, newReview):
        query = """
            SELECT id FROM albums WHERE name='%s'
        """ % escape(newReview['album'])
        album = self.sqlFetchOne(query)
        if album:
            newReview['album_id'] = album[0]
        matches = """
            artist_id='%s' AND link='%s'
        """ % (newReview['artist_id'], escape(newReview['link']))
        return self._update(newReview, 'reviews', matches)
        
class MetalArchives(Data):

    def update_review(self, newReview):
        query = """
            SELECT id FROM albums WHERE name='%s'
         """ % escape(newReview['album'])
        album = self.sqlFetchOne(query)
        if album:
            newReview['album_id'] = album[0]
        matches = """
            artist_id='%s' AND link='%s'
        """ % (newReview['artist_id'], escape(newReview['link']))
        return self._update(newReview, 'reviews', matches)

class MetalReview(Data):

    def update_review(self, newReview):
        query = """
            SELECT id FROM albums WHERE name='%s'
        """ % escape(newReview['album'])
        album = self.sqlFetchOne(query)
        if album:
            newReview['album_id'] = album[0]
        matches = """
            artist_id='%s' AND link='%s'
        """ % (newReview['artist_id'], escape(newReview['link']))
        return self._update(newReview, 'reviews', matches)

class Lambgoat(Data):

    def update_news(self, newNews):
        matches = """
            artist_id='%s' AND link='%s'
        """ % (newNews['artist_id'], escape(newNews['link']))
        return self._update(newNews, 'news', matches)

    def update_review(self, newReview):
        query = """
            SELECT id FROM albums WHERE name='%s'
        """ % escape(newReview['album'])
        album = self.sqlFetchOne(query)
        if album:
            newReview['album_id'] = album[0]
        matches = """
            artist_id='%s' AND link='%s'
        """ % (newReview['artist_id'], escape(newReview['link']))
        return self._update(newReview, 'reviews', matches)

