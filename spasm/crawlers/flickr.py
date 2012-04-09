SLEEP = 60 # 1 minute

import spasm.data.sources as _data
import spasm.web.sources as _web
import time

Data = _data.Flickr()
Web = _web.Flickr()

def run(artist):

    web2data = (
        (Web.search_photos, Data.update_photo),)

    if not artist['ambiguous']:

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
