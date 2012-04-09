SLEEP = 60 # 1 minute

import spasm.data.sources as _data
import spasm.web.sources as _web
import time

Data = _data.Google()
Web = _web.Google()

def run(artist):

    # Update reviews
    albums = Data.get_albums(artist)[:8]

    for album in albums:
        if len(album['name']) > 3:
            results = Web.search_reviews(artist, album)
            for result in results:
                Data.update_review(result)

    # Update interviews 
    if not artist['ambiguous']:
        results = Web.search_interviews(artist)
        for result in results:
            Data.update_interview(result)

            
if __name__ == "__main__":
    while True:
        artists = Data.get_artists()
        for artist in artists:
            run(artist)
        time.sleep(SLEEP)
