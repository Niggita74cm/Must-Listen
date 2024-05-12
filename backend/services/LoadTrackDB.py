import pandas as pd
from sqlalchemy.orm import Session
from backend.model.models_admin import LoadTrack
from backend.database.work_db_track import create_track

def LoadTrackDB(name_database: str, db: Session):
    df = pd.read_csv(name_database)
    print(df.head())
    for index, row in df.iterrows():
        track = LoadTrack(
            track_name=row["track_name"],
            artists=row["artists"],
            album_name=row["album_name"],
            popularity=row["popularity"],
            duration_ms=row["duration_ms"],
            explicit=row["explicit"],
            danceability=row["danceability"],
            energy=row["energy"],
            key=row["key"],
            loudness=row["loudness"],
            mode=row["mode"],
            speechiness=row["speechiness"],
            acousticness=row["acousticness"],
            instrumentalness=row["instrumentalness"],
            liveness=row["liveness"],
            valence=row["valence"],
            tempo=row["tempo"],
            time_signature=row["time_signature"],
            track_genre=row["track_genre"],
            picture_track=row["link_picture"]
        )
        create_track(db=db, track=track)