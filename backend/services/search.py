from difflib import SequenceMatcher
from backend.model.models_action import SearchResults
def find_similar_strings(target, string, threshold=0.2):
    similarity_ratio = SequenceMatcher(None, target, string).ratio()
    if similarity_ratio >= threshold:
        return (True, similarity_ratio)
    else:
        return (False, similarity_ratio)

def search_tracks(searched_str:str, search_all_track):
    print("search_tracks")
    found_tracks = []
    for track in search_all_track:
        print(f'track: {track}')
        founded_track = SearchResults(
            track_id=track.id,
            track_name=track.track_name,
            album_name=track.album_name,
            artists=track.artists,
            popularity=track.popularity,
            rating=track.rating
        )

        result_1 = find_similar_strings(searched_str, track.track_name)
        result_2 = find_similar_strings(searched_str, track.artists)
        result_3 = find_similar_strings(searched_str, track.album_name)
        if result_1[0] == True:
            found_tracks.append((founded_track, result_1[1]))
        if result_2[0] == True:
            found_tracks.append((founded_track, result_2[1]))
        if result_3[0] == True:
            found_tracks.append((founded_track, result_3[1]))
    sorted_results = sorted(found_tracks, key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_results]

def SortSimilarity():
    ...
