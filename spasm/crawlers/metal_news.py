SLEEP = 900 # 15 min

import spyder.data.metal_sources as _data
import spyder.web.metal_sources as _web

import re
import time

Sources = [
    (_web.Blabbermouth(), _data.Blabbermouth()),
    (_web.Lambgoat(), _data.Lambgoat())]
     
def _valid(title, artist):
    p = re.compile(r'(?:^|\s)%s(?:$|\s|[:])' % artist['name'].lower())
    matches = p.findall(title.lower())
    return True if matches else False

def _run():
    for web, data in Sources:
        news = web.get_latest_news()
        artists = data.get_artists()
        for n in news:
            for artist in artists:
                if _valid(n['title'], artist):
                    n['artist_id'] = artist['id']
                    data.update_news(n)
                    break
            
if __name__ == "__main__":
    while True:
        _run()
        time.sleep(SLEEP)