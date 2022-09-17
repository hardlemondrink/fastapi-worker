from enum import unique
import sqlalchemy as sa
import sqlalchemy.types as types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import DATETIME
from decimal import Decimal as D

Base = declarative_base()


class SqliteNumeric(types.TypeDecorator):
    impl = types.String
    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(types.VARCHAR(100))
    def process_bind_param(self, value, dialect):
        return str(value)
    def process_result_value(self, value, dialect):
        return D(value)

Numeric = SqliteNumeric


class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(DATETIME(fsp=6))
    kind = sa.Column(sa.String)
    amount = sa.Column(Numeric(10, 2))
    description = sa.Column(sa.String, nullable=True)


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    isActive = sa.Column(sa.Boolean)
    login = sa.Column(sa.String)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    email = sa.Column(sa.String)
    phoneNumber = sa.Column(sa.String) # localized  format 79991112233
    country = sa.Column(sa.String)
    registration_type = sa.Column(sa.String) # VK ID / Yandex ID / Apple ID / E-Mail / Phone / Google ID
    registration_date = sa.Column(DATETIME(fsp=6))


class Token(Base):
    __tablename__ = 'tokens'

    id = sa.Column(sa.Integer, primary_key=True)
    token = sa.Column(
        sa.UUID(as_uuid=False), 
        server_default=sa.text('uuid_generate_v4()'), 
        unique=True, 
        nullable=False, 
        index=False)