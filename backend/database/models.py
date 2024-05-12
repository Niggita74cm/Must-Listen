from sqlalchemy.orm import relationship
from backend.database.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Boolean, Text, Float, TIMESTAMP
class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    auth2 = Column(Boolean, nullable=False)
    __table_args__ = (
        UniqueConstraint('login', 'hashed_password', name='unique_login_passwd'),
    )


class Track(Base):
    #artists,album_name,track_name,popularity,duration_ms,explicit,danceability,energy,key,loudness,mode,
    #speechiness,acousticness,instrumentalness,liveness,valence,tempo,time_signature,track_genre
    id = Column(Integer, primary_key=True, index=True)
    track_name = Column(String, nullable=False)
    artists = Column(String, nullable=False)
    album_name = Column(String, nullable=False)
    popularity = Column(Integer, nullable=False)
    duration_ms = Column(Integer, nullable=False)
    explicit = Column(Boolean, nullable=False)
    danceability = Column(Float, nullable=False)
    energy = Column(Float, nullable=False)
    key = Column(Integer, nullable=False)
    loudness = Column(Float, nullable=False)
    mode = Column(Integer, nullable=False)
    speechiness = Column(Float, nullable=False)
    acousticness = Column(Float, nullable=False)
    instrumentalness = Column(Float, nullable=False)
    liveness = Column(Float, nullable=False)
    valence = Column(Float, nullable=False)
    tempo = Column(Float, nullable=False)
    time_signature = Column(Integer, nullable=False)
    track_genre = Column(String, nullable=False)
    picture_track = Column(String)
    rating = Column(Float, nullable=False)
class User_track(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    track_id = Column(Integer, ForeignKey('track.id'), nullable=False)
    ratingSelf = Column(Float, nullable=False)
    date = Column(TIMESTAMP, nullable=False)

    user = relationship('User', remote_side='User_track.user_id')
    track = relationship('Track', remote_side='User_track.track_id')

class Comment(Base):
     id = Column(Integer, primary_key=True, index=True)
     comment = Column(Text, nullable=False)
     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
     track_id = Column(Integer, ForeignKey('track.id'), nullable=False)
     user = relationship('User', remote_side='Comment.user_id')
     track = relationship('Track', remote_side='Comment.track_id')


