from spasm.data.core import Data
from spasm.data.util import *

import time
WEEKLY = 604800

class Google(Data):

    def update_review(self, newReview):
        matches = """
            artist_id=%s AND url=%s
        """ % (newReview['artist_id'], escape(newReview['url'], 'url'))
        return self._update(newReview, 'reviews', matches)

    def update_interview(self, newInterview):
        matches = """
            artist_id=%s AND url=%s
        """ % (newInterview['artist_id'], escape(newInterview['url'], 'url'))
        return self._update(newInterview, 'interviews', matches)


class Twitter(Data):
    
    def update_news(self, newNews):
        matches = """
            artist_id=%s AND url=%s
        """ % (newNews['artist_id'], escape(newNews['url'], 'url'))
        return self._update(newNews, 'news', matches)

    def add_stats(self, stats):
        fields = [escape(stats[field], field) for field in stats]
        query1 = ','.join(fields)
        query = """
            INSERT INTO twitter_stats (%s) VALUES (%s)
        """ % (','.join(stats.keys()), query1)
        self.sqlExecute(query)


class Flickr(Data):

    def update_photo(self, newPhoto):
        matches = """
            artist_id=%s AND url=%s
        """ % (newPhoto['artist_id'], escape(newPhoto['url'], 'url'))
        return self._update(newPhoto, 'photos', matches)


class LastFM(Data):

    def add_stats(self, stats):
        fields = [escape(stats[field], field) for field in stats]
        query1 = ','.join(fields)
        query = """
            INSERT INTO lastfm_stats (%s) VALUES (%s)
        """ % (','.join(stats.keys()), query1)
        self.sqlExecute(query)

    def update_artist(self, artist):
        fields = ["%s=%s" % (field, escape(artist[field], field)) for field in artist]
        query1 = ','.join(fields)
        query = """
            UPDATE artists SET %s WHERE id=%s
        """ % (query1, artist['id'])
        self.sqlExecute(query)
        
    def get_artist_stats(self, artist, since=None, now=None):
        if not since:
            since = WEEKLY
        if not now:
            now = time.time()
        now1 = time.gmtime(now)
        since1 = time.gmtime(now - since)
        query = """
            SELECT listeners, playcount, date FROM lastfm_stats 
            WHERE artist_id=%s AND date < \'%s\' ORDER BY date DESC LIMIT 1
        """ % (artist['id'], time.strftime('%Y-%m-%d %H:%M:%S', now1))
        now = self.sqlFetchOne(query)
        query = """
            SELECT listeners, playcount FROM lastfm_stats 
            WHERE artist_id=%s AND date < \'%s\' ORDER BY date DESC LIMIT 1
        """ % (artist['id'], time.strftime('%Y-%m-%d %H:%M:%S', since1))
        since1 = self.sqlFetchOne(query)
        if now and since1:
            diff = tuple([now[0] - since1[0], now[1] - since1[1]])
            return {
                'date'      : now[2],
                'listeners' : tuple([
                    diff[0] if diff[0] > 0 else 0, 
                    float(diff[0]) / since1[0] if since1[0] != 0 else None]),
                'playcount' : tuple([
                    diff[1] if diff[1] > 0 else 0, 
                    float(diff[1]) / since1[1] if since1[1] != 0 else None])
                }
        else:
            return {
                'listeners': (None, None),
                'playcount': (None, None)
            }

    def update_album(self, newAlbum):
        matches = """
            artist_id=%s AND name=%s
        """ % (newAlbum['artist_id'], escape(newAlbum['name']))
        return self._update(newAlbum, 'albums', matches)
        
    def update_track(self, newTrack):
        matches = """
            artist_id=%s AND name=%s
        """ % (newTrack['artist_id'], escape(newTrack['name']))
        return self._update(newTrack, 'tracks', matches)
        
    def update_tag(self, newTag):
        if 'name' in newTag:
            matches = """
                artist_id=%s AND name=%s
            """ % (newTag['artist_id'], escape(newTag['name']))
            return self._update(newTag, 'tags', matches)
            
    def update_similar(self, newSimilar):
        matches = """
            artist_id=%s AND name=%s
        """ % (newSimilar['artist_id'], escape(newSimilar['name']))
        return self._update(newSimilar, 'similar', matches)


class MySpace(Data):

    def add_stats(self, stats):
        # Myspace hack - unpredictable stats scraping behavior
        now1 = time.gmtime(time.time())
        query = """
            SELECT plays, views, fans FROM myspace_stats 
            WHERE artist_id=%s AND date < \'%s\' ORDER BY id DESC LIMIT 1
        """ % (stats['artist_id'], time.strftime('%Y-%m-%d %H:%M:%S', now1))
        result = self.sqlFetchOne(query)
        prev = dict(zip(['plays','views','fans'], result)) if result else None
        if not prev or (int(stats['plays']) >= int(prev['plays']) 
                and int(stats['views']) >= int(prev['views'])):
            fields = [escape(stats[field], field) for field in stats]
            query1 = ','.join(fields)
            query = """
                INSERT INTO myspace_stats (%s) VALUES (%s)
            """ % (','.join(stats.keys()), query1)
            self.sqlExecute(query)
        else:
            print """
                (%s) WARNING: MySpace stats look sketchy, ignoring...
                Found Myspace stats: %s
                Previous Myspace stats: %s
            """ % (time.ctime(), stats, prev)
            
    def update_show(self, newShow):
        matches = """
            artist_id=%s AND DATE_FORMAT(date,'%%Y-%%m-%%d')='%s'
        """ % (newShow['artist_id'], newShow['date'].strftime('%Y-%m-%d'))
        return self._update(newShow, 'shows', matches)

    def update_news(self, newNews):
        matches = """
            artist_id=%s AND url=%s
        """ % (newNews['artist_id'], escape(newNews['url']))
        return self._update(newNews, 'news', matches)

    def get_artist_stats(self, artist, since=None, now=None):
        if not since:
            since = WEEKLY
        if not now:
            now = time.time()
        now1 = time.gmtime(now)
        since1 = time.gmtime(now - since)
        since2 = time.gmtime(now - since*2)
        query = """
            SELECT plays, views, fans FROM myspace_stats 
            WHERE artist_id=%s AND date < \'%s\' ORDER BY id DESC LIMIT 1
        """ % (artist['id'], time.strftime('%Y-%m-%d %H:%M:%S', now1))
        now = self.sqlFetchOne(query)
        query = """
            SELECT plays, views, fans FROM myspace_stats 
            WHERE artist_id=%s AND date < \'%s\' ORDER BY id DESC LIMIT 1
        """ % (artist['id'], time.strftime('%Y-%m-%d %H:%M:%S', since1))
        since1 = self.sqlFetchOne(query)
        if now and since1:
            diff = tuple([now[0] - since1[0], now[1] - since1[1], now[2] - since1[2]])
            return {
                'plays' : tuple([
                    diff[0], 
                    float(diff[0]) / since1[0] if since1[0] != 0 else None]),
                'views' : tuple([
                    diff[1], 
                    float(diff[1]) / since1[1] if since1[1] != 0 else None]),
                'fans'  : tuple([
                    diff[2], 
                    float(diff[2]) / since1[2] if since1[2] != 0 else None])
                }
        else:
            return {
                'plays': (None, None),
                'views': (None, None),
                'fans' : (None, None)
            }
            

class BTJunkie(Data):

    def add_stats(self, torrent):
        query = """
            SELECT id, artist_id FROM torrents WHERE url=%s
        """ % escape(torrent['url'])
        t = self.sqlFetchOne(query)
        if t:
            query = """
                INSERT INTO torrent_stats (torrent_id, artist_id, leechers, seeds) 
                VALUES (%s, %s, %s, %s)
            """ % (t[0], t[1], torrent['leechers'], torrent['seeds'])
            self.sqlExecute(query)

    def update_torrent(self, newTorrent):
        matches = """
            artist_id=%s AND url=%s
        """ % (newTorrent['artist_id'], escape(newTorrent['url']))
        self._update(newTorrent, 'torrents', matches)
        self.add_stats(newTorrent)

    def get_artist_stats(self, artist, since=None, now=None):
        if not since:
            since = WEEKLY
        if not now:
            now = time.time()

        now1 = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(now))
        since1 = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(now - since))
        since2 = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(now - since*2))
        query = """
            SELECT MAX(seeds), MAX(leechers) FROM torrent_stats 
            WHERE artist_id=%s AND date > \'%s\' AND date < \'%s\' 
            GROUP BY torrent_id 
            ORDER BY date'
        """ % (artist['id'], since1, now1)
        s1 = self.sqlFetchAll(query)
        query = """
            SELECT MAX(seeds), MAX(leechers) FROM torrent_stats 
            WHERE artist_id=%s AND date > \'%s\' AND date < \'%s\' 
            GROUP BY torrent_id 
            ORDER BY date
        """ % (artist['id'], since2, since1)
        s2 = self.sqlFetchAll(query)

        since1 = [0 if s1 else None, 0 if s1 else None]
        since2 = [0 if s2 else None, 0 if s2 else None]
        for row in s1:
            since1[0] += int(row[0]) if row and row[0] else 0
            since1[1] += int(row[1]) if row and row[1] else 0
        for row in s2:
            since2[0] += int(row[0]) if row and row[0] else 0
            since2[1] += int(row[1]) if row and row[1] else 0
        return {
            'seeds': tuple([
                since1[0],
                float(since1[0] - since2[0]) / since2[0] if since2[0] and since1[0] else None]),
            'leechers' :  tuple([
                since1[1],
                float(since1[1] - since2[1]) / since2[1] if since2[1] and since1[1] else None])
        }


class YouTube(Data):

    def add_stats(self, video):
        query = """
            SELECT id, artist_id FROM videos WHERE url=%s
        """ % escape(video['url'])
        t = self.sqlFetchOne(query)
        if t:
            query = """
                INSERT INTO youtube_stats (video_id, artist_id, views) 
                VALUES (%s, %s, %s)
            """ % (t[0], t[1], video['views'])
            self.sqlExecute(query)

    def update_video(self, newVideo):
        matches = """
            artist_id=%s AND url=%s
        """ % (newVideo['artist_id'], escape(newVideo['url']))
        self._update(newVideo, 'videos', matches)
        self.add_stats(newVideo)

    def update_thumbnail(self, video, thumbnail):
        query = """
            UPDATE videos SET thumbnail='%s' WHERE id=%s
        """ % (thumbnail, video['id'])
        self.sqlExecute(query)

    def get_artist_stats(self, artist, since=None, now=None):
        if not since:
            since = WEEKLY
        if not now:
            now = time.time()
        now1 = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(now))
        since1 = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(now - since))
        since2 = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(now - since*2))
        query = """
            SELECT MAX(views) FROM youtube_stats 
            WHERE artist_id=%s AND date > \'%s\' AND date < \'%s\' 
            GROUP BY video_id
        """ % (artist['id'], since1, now1)
        s1 = self.sqlFetchAll(query)
        if s1:
            s1 = [int(s[0]) for s in s1 if s and s[0]]
            s1 = reduce(lambda x,y: x+y, s1)/len(s1) if s1 else None
        else:
            s1 = None
        query = """
            SELECT MAX(views) FROM youtube_stats 
            WHERE artist_id=%s AND date > \'%s\' AND date < \'%s\' 
            GROUP BY video_id
        """ % (artist['id'], since2, since1)
        s2 = self.sqlFetchAll(query)
        if s2:
            s2 = [int(s[0]) for s in s2 if s and s[0]]
            s2 = reduce(lambda x,y: x+y, s2)/len(s2) if s2 else None
        else:
            s2 = None
        return {
            'views': tuple([
                s1 - s2 if s1 and s2 else None,
                float(s1 - s2) / s2 if s2 and s1 else None])
        }


class TinySong(Data):

    def update_audio(self, newAudio):
        matches = """
            artist_id=%s AND url=%s
        """ % (newAudio['artist_id'], escape(newAudio['url'], 'url'))
        return self._update(newAudio, 'audio', matches) 
