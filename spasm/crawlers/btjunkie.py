SLEEP = 60 * 15 # 15 minutes

import spasm.data.sources as _data
import spasm.web.sources as _web
import time

Data = _data.BTJunkie()
Web = _web.BTJunkie()

def run(artist):

    # Get filter terms
    albums = Data.get_albums(artist)
    filter_terms = [album['name'] for album in albums]
    
    # Update torrents
    web2data = (
        (Web.search_torrents, Data.update_torrent, {'filter_terms': filter_terms}),)
        
    for web, data, kwargs in web2data:
        kwargs = kwargs if artist['ambiguous'] else {}
        dd = web(artist, **kwargs)
        for d in dd:
            data(d)
        
if __name__ == "__main__":
    while True:
        artists = Data.get_artists()
        for artist in artists:
            run(artist)
        time.sleep(SLEEP)
