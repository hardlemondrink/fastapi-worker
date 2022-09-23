import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.dialects.mysql import DATETIME

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text, unique=True)
    username = sa.Column(sa.Text, unique=True)
    password_hash = sa.Column(sa.Text)
    isActive = sa.Column(sa.Boolean)


class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    date = sa.Column(sa.DateTime)
    kind = sa.Column(sa.String)
    description = sa.Column(sa.String, nullable=True)
    isActive = sa.Column(sa.Boolean)


class Booking(Base):
    __tablename__ = 'booking'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    created_at = sa.Column(sa.DateTime, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    book_type = sa.Column(sa.String, nullable=False)
    address = sa.Column(sa.String)
    price = sa.Column(sa.Float)
    country = sa.Column(sa.String, nullable=False)
    city = sa.Column(sa.String, nullable=False)
    phoneNumber = sa.Column(sa.String)
    isActive = sa.Column(sa.Boolean, nullable=False)


class Pictures(Base):
    __tablename__ = 'pictures'

    id = sa.Column(sa.Integer, primary_key=True)
    path = sa.Column(sa.String, nullable=False)
    booking_id = sa.Column(sa.Integer, nullable=False)


class Reservation(Base):
    __tablename__ = 'reservations'

    id = sa.Column(sa.Integer, primary_key=True)
    booking_id = sa.Column(sa.Integer)
    created_at = sa.Column(sa.DateTime)
    user_id = sa.Column(sa.Integer)
    booking_expiration = sa.Column(sa.DateTime)
    isActive = sa.Column(sa.Boolean)
