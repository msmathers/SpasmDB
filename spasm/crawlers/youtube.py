SLEEP = 900 # 15 min

import spasm.data.sources as _data
import spasm.web.sources as _web
import time

Data = _data.YouTube()
Web = _web.YouTube()

def run(artist):

    # Get filter terms
    filter_terms = Data.get_filter_terms(artist)

    videos = Web.search_videos(artist, filter_terms=filter_terms)
    for video in videos:
        Data.update_video(video)

    if artist['youtube_url']:
        videos = Web.get_videos(artist)
        for video in videos:
            Data.update_video(video)	
    
            
if __name__ == "__main__":
    while True:
        artists = Data.get_artists()
        for artist in artists:
            run(artist)
        time.sleep(SLEEP)
