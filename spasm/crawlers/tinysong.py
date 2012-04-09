SLEEP = 60 # 1 minute

import spasm.data.sources as _data
import spasm.web.sources as _web
import time

Data = _data.TinySong()
Web = _web.TinySong()

def run(artist):

    # Get tracks
    tracks = Data.get_tracks(artist)

    for track in tracks[:12]:
        results = Web.search_audio_tracks(artist, track)
        for result in results:
            Data.update_audio(result)

            
if __name__ == "__main__":
    while True:
        artists = Data.get_artists()
        for artist in artists:
            run(artist)
        time.sleep(SLEEP)
