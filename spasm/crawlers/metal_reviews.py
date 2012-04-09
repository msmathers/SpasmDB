SLEEP = 900 # 15 min

import spyder.data.metal_sources as _data
import spyder.web.metal_sources as _web

import time

Sources = [
    (_web.Blabbermouth(), _data.Blabbermouth()),
    (_web.Lambgoat(), _data.Lambgoat()),
    (_web.MetalArchives(), _data.MetalArchives()),
    (_web.MetalReview(), _data.MetalReview())]

def _run():
    for web, data in Sources:
        reviews = web.get_latest_reviews()
        artists = data.get_artists()
        for review in reviews:
            for artist in artists:
                if review['artist'].lower() == artist['name'].lower():
                    review['artist_id'] = artist['id']
                    data.update_review(review)
                    break
            
if __name__ == "__main__":
    while True:
        _run()
        time.sleep(SLEEP)