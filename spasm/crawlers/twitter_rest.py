SLEEP = 60 # 1 minute

import spasm.data.sources as _data
import spasm.web.sources as _web
import time

Data = _data.Twitter()
Web = _web.Twitter()

def run(artist):

    if artist['twitter_url']:

        web2data = (
            (Web.get_news, Data.update_news),
            (Web.get_stats, Data.add_stats),)

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
