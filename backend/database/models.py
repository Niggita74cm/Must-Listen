from sqlalchemy.orm import relationship
from backend.database.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Boolean, Text, Float
class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    auth2 = Column(Boolean, nullable=False)
    __table_args__ = (
        UniqueConstraint('login', 'hashed_password', name='unique_login_passwd'),
    )

class User_data(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    user = relationship('User',  remote_side = 'User_data.user_id')

class Track(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type_track = Column(String, nullable=False)
    data_track = Column(Text, nullable=False)
class User_track(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    track_id = Column(Integer, ForeignKey('track.id'), nullable=False)
    rating = Column(Float, nullable=False)
    user = relationship('User', remote_side='User_track.user_id')
    track = relationship('Track', remote_side='User_track.track_id')

class Comment(Base):
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    track_id = Column(Integer, ForeignKey('track.id'), nullable=False)
    user = relationship('User', remote_side='User_track.user_id')
    track = relationship('Track', remote_side='User_track.track_id')
