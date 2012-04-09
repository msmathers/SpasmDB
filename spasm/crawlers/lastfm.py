SLEEP = 21600 # 6 hours

import spasm.data.sources as _data
import spasm.web.sources as _web
import time

Data = _data.LastFM()
Web = _web.LastFM()

def run(artist):

    # Update name, thumbnail, metadata
    _artist = Web.get_artist(artist)
    for field in _artist:
        if field in artist:
            artist[field] = _artist[field]
    Data.update_artist(artist)
    
    # Update stats
    Data.add_stats({
        'artist_id' : artist['id'],
        'listeners' : _artist['listeners'],
        'playcount' : _artist['playcount']
    })
    
    # Update albums, tracks, tags, similar
    web2data = (
        (Web.get_top_albums, Data.update_album),
        (Web.get_top_tracks, Data.update_track),
        (Web.get_top_tags, Data.update_tag),
        (Web.get_similar_artists, Data.update_similar))
        
    for web, data in web2data:
        dd = web(artist)
        for d in dd:
            data(d)
            
            
if __name__ == "__main__":
    while True:
        artists = Data.get_artists()
        for artist in artists:
            run(artist)
        time.sleep(SLEEP)
