import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import DATETIME

Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(DATETIME(fsp=6))
    kind = sa.Column(sa.String)
    description = sa.Column(sa.String, nullable=True)