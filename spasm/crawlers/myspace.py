SLEEP = 900 # 15 min

import spasm.data.sources as _data
import spasm.web.sources as _web
import time

Data = _data.MySpace()
Web = _web.MySpace()

def run(artist):

    if artist['myspace_url']:
    
        # Update stats, shows, news
        web2data = (
            (Web.get_stats, Data.add_stats),
            (Web.get_shows, Data.update_show),
            (Web.get_news, Data.update_news))
        
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
