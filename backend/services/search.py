from difflib import SequenceMatcher
from backend.model.models_action import SearchResults
def find_similar_strings(target, string, threshold=0.7):
    similarity_ratio = SequenceMatcher(None, target, string).ratio()
    if similarity_ratio >= threshold:
        return (True, similarity_ratio)
    else:
        return (False, similarity_ratio)

def search_tracks(string:str, all_tracks):
    found_tracks = []
    for track in all_tracks:
        result_1 = find_similar_strings(string, track.track_name)
        result_2 = find_similar_strings(string, track.artists)
        result_3 = find_similar_strings(string, track.album_name)
        if result_1[0] == True or result_2[0] == True or result_3[0] == True:
            founded_track = SearchResults(
                track_name=track.track_name,
                album_name=track.album_name,
                artists=track.artists,
                rating=track.rating
            )
            found_tracks.append(founded_track)
    return found_tracks

