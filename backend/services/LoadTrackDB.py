import pandas as pd
from sqlalchemy.orm import Session
from backend.model.models_admin import LoadTrack
from backend.database.work_db_track import create_track
import numpy as np
def LoadTrackDB(name_database: str, db: Session):
    df = pd.read_csv(name_database)
    print(df.head())
    df['picture_track'] = ""
    for index, row in df.iterrows():
        if row["track_name"] is np.nan or row["artists"] is np.nan or row["album_name"] is np.nan:
            continue
        if row["popularity"] is np.nan or row["duration_ms"] is np.nan or row["explicit"] is np.nan:
            continue
        if row["danceability"] is np.nan or row["energy"] is np.nan or row["key"] is np.nan:
            continue
        if row["loudness"] is np.nan or row["mode"] is np.nan or row["speechiness"] is np.nan:
            continue
        if row["valence"] is np.nan or row["tempo"] is np.nan or row["time_signature"] is np.nan or row["track_genre"] is np.nan:
            continue
        if row["acousticness"] is np.nan or row["instrumentalness"] is np.nan or row["liveness"] is np.nan:
            continue
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
            picture_track=row["picture_track"]
        )
        create_track(db=db, track=track)
