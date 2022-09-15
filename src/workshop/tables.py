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