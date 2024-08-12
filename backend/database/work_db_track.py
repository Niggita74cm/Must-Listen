from backend.database.models import Track
from backend.model.models_admin import LoadTrack
from sqlalchemy.orm import Session
from sqlalchemy import update
# Use with database Track
def create_track(db: Session, track: LoadTrack):
    createTrack = Track(
        track_name=track.track_name,
        artists=track.artists,
        album_name=track.album_name,
        popularity=track.popularity,
        duration_ms=track.duration_ms,
        explicit=track.explicit,
        danceability=track.danceability,
        energy=track.energy,
        key=track.key,
        loudness=track.loudness,
        mode=track.mode,
        speechiness=track.speechiness,
        acousticness=track.acousticness,
        instrumentalness=track.instrumentalness,
        liveness=track.liveness,
        valence=track.valence,
        tempo=track.tempo,
        time_signature=track.time_signature,
        track_genre=track.track_genre,
        picture_track=track.picture_track,
        rating=0.0,
        number_rating=0
    )
    db.add(createTrack)
    db.commit()
    db.refresh(createTrack)
    return createTrack


def get_all_track(db: Session):
    all_data = db.query(Track.id, Track.track_name, Track.artists, Track.album_name, Track.rating, Track.popularity).all()
    return all_data
def get_track(db: Session, track_id: int):
    track = db.query(Track).filter(Track.id == track_id).first()
    return track
def search_track_by_name(db: Session, name_track: str):
    firstQuery = name_track+'%'
    tracks = db.query(Track).filter(Track.track_name.like(firstQuery)).all()
    secondQuery = "% "+name_track+'%'
    tracks += db.query(Track).filter(Track.track_name.like(secondQuery)).all()
    print(f"len tracks by name: {len(tracks)}")
    return tracks
def search_track_by_album(db: Session, album_track: str):
    firstQuery = album_track + '%'
    tracks = db.query(Track).filter(Track.album_name.like(firstQuery)).all()
    secondQuery = "% " + album_track + '%'
    tracks += db.query(Track).filter(Track.album_name.like(secondQuery)).all()
    print(f"len tracks by album: {len(tracks)}")
    return tracks
def search_track_by_artists(db: Session, artists_track: str):
    firstQuery = artists_track + '%'
    tracks = db.query(Track).filter(Track.artists.like(firstQuery)).all()
    secondQuery = "% " + artists_track + '%'
    tracks += db.query(Track).filter(Track.artists.like(secondQuery)).all()
    print(f"len tracks by artists: {len(tracks)}")
    return tracks
def search_track(db: Session, name_track: str, artists_track: str, albums_track: str):
    tracks = search_track_by_name(db, name_track)
    tracks += search_track_by_album(db, albums_track)
    tracks += search_track_by_artists(db, artists_track)
    return tracks
def update_rating(db: Session, track_id: int, rating: float):
    db.execute(update(Track).where(Track.id == track_id).values(rating=rating))
    db.commit()
    user = db.query(Track).filter(Track.id == track_id).first()
    db.refresh(user)

def update_num_rating(db: Session, track_id: int, number_rating: int):
    db.execute(update(Track).where(Track.id == track_id).values(number_rating=number_rating))
    db.commit()
    user = db.query(Track).filter(Track.id == track_id).first()
    db.refresh(user)