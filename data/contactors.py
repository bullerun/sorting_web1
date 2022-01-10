import sqlalchemy
from .db_session import SqlAlchemyBase


class Contactors(SqlAlchemyBase):
    __tablename__ = 'Contactors'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    vendor_code = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    manufacturer = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    rated_V = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    rated_A = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
