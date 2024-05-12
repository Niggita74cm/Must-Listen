from difflib import SequenceMatcher
from backend.model.models_action import SearchResults
def find_similar_strings(target, string, threshold=0.7):
    similarity_ratio = SequenceMatcher(None, target, string).ratio()
    if similarity_ratio >= threshold:
        return True
    else:
        return False

def search_tracks(string:str, all_tracks):
    found_tracks = []
    for track in all_tracks:
        if find_similar_strings(string, track.track_name) == True:
            founded_track = SearchResults(
                track_name=track.track_name,
                album_name=track.album_name,
                artists=track.artists,
                rating=track.rating
            )
            found_tracks.append(founded_track)
    return found_tracks

