import MySQLdb

from spasm.data.config import *
from spasm.data.util import *

def _cursor(func):
    def _d(obj, query):
        cur = obj.con.cursor()
        cur.execute(safe_str(query))
        result = func(obj, query, **{'cur': cur})
        cur.close() 
        obj.con.commit()
        return result
    return _d

class SQL():

    def __init__(self):
        self.con = MySQLdb.connect(**CONFIG)
        
    @_cursor
    def sqlExecute(self, query, **kwargs):
        return True

    @_cursor
    def sqlFetchOne(self, query, **kwargs):
        if 'cur' in kwargs and kwargs['cur'].rowcount:
            return kwargs['cur'].fetchone()
        else:
            return None

    @_cursor 
    def sqlFetchAll(self, query, **kwargs):
        if 'cur' in kwargs and kwargs['cur'].rowcount:
            return kwargs['cur'].fetchall() 
        else:
            return []


class Data(SQL):

    FIELDS = [
        'id','name','slug','mbid','lastfm_url','myspace_url','twitter_url','facebook_url',
        'youtube_url', 'website_url', 'image_small', 'image_medium', 'image_large','ambiguous']

    def get_artists(self, fields=FIELDS, order_by='name'):
        query = """
            SELECT %s FROM artists ORDER BY %s
        """ % (','.join(fields), order_by)
        result = self.sqlFetchAll(query)
        artists = [dict(zip(fields,artist)) for artist in result]
        return artists
        
    def get_artist(self, id=None, slug=None, fields=FIELDS, order_by='name'):
        if id:
            query = """
                SELECT %s FROM artists WHERE id=%s
            """ % (','.join(fields), id)
        elif slug:
            query = """
                SELECT %s FROM artists WHERE slug='%s'
            """ % (','.join(fields), slug)
        else:
            return None
        result = self.sqlFetchOne(query)
        artist = dict(zip(fields,result))
        return artist

    def get_albums(self, artist):
        fields = ['id','added','name','url','mbid','playcount',
            'image_small','image_medium','artist_id']
        query = """
            SELECT %s FROM albums WHERE artist_id=%s ORDER BY id
        """ % (",".join(fields), artist['id'])
        results = self.sqlFetchAll(query)
        albums = [dict(zip(fields,result)) for result in results]
        return albums

    def get_tracks(self, artist):
        fields = ['id','added','name','url','mbid','listeners','artist_id']
        query = """
            SELECT %s FROM tracks WHERE artist_id=%s ORDER BY id
        """ % (",".join(fields), artist['id'])
        results = self.sqlFetchAll(query)
        albums = [dict(zip(fields,result)) for result in results]
        return albums
        
    def get_filter_terms(self, artist):
        query = """
            SELECT name FROM albums WHERE artist_id=%s
        """ % artist['id']
        results = self.sqlFetchAll(query)
        albums = [album[0].lower() for album in results\
            if len(album[0]) > 3 and album[0].lower() != artist['name'].lower()]
        query = """
            SELECT name FROM tracks WHERE artist_id=%s
        """ % artist['id']
        results = self.sqlFetchAll(query)
        tracks = [track[0].lower() for track in results\
            if len(track[0]) > 3 and track[0].lower() != artist['name'].lower()]
        terms = list(set(albums + tracks))
        #if not terms:
        #    terms = [artist['name'].lower()]
        return terms
        
    def _update(self, dict, table, where):
        exists = self.sqlFetchOne("SELECT id FROM %s WHERE %s" % (table, where))
        if not exists:
            fields = [escape(dict[field], field) for field in dict]
            query1 = ','.join(fields)
            query = """
                INSERT INTO %s (%s) VALUES (%s)
            """ % (table, ','.join(dict.keys()), query1)
        else:
            fields = ["%s=%s" % (field, escape(dict[field], field)) for field in dict]
            query1 = ','.join(fields)
            query = """
                UPDATE %s SET %s WHERE id=%s
            """ % (table, query1, exists[0])
        try:
            self.sqlExecute(query)
            return not exists
        except:
            print "(%s) Failed to update on query: %s" % (time.ctime(), safe_str(query))

    def update_stats(self, artist, job_id, average_change, type='weekly', **kwargs):
        q1 = [escape(kwargs[field][0], field) for field in kwargs]
        q2 = [escape(kwargs[field][1], field) for field in kwargs]
        query1 = ','.join(map(lambda x: "'%s'" % x if x is not None else 'null', q1))
        query2 = ','.join(map(lambda x: "'%s'" % x if x is not None else 'null', q2))
        fields1 = ','.join(kwargs.keys())
        fields2 = ','.join(['%s_change' % key for key in kwargs.keys()])
        query = '%s,%s' % (query1, query2)
        fields = '%s,%s' % (fields1, fields2)
        query = """
            INSERT INTO stats_%s (artist_id, job_id, average_change, %s) 
            VALUES (%s, %s, %s, %s)
        """ % (type, fields, artist['id'], job_id, 
               average_change if average_change is not None else 'null', 
               query)
        self.sqlExecute(query)
