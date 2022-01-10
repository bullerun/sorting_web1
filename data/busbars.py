import sqlalchemy
from .db_session import SqlAlchemyBase


class Busbars(SqlAlchemyBase):
    __tablename__ = 'Copper busbars'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    vendor_code = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    manufacturer = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    type_size = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    rated_KW = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    rated_A = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    width_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    width_height = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    width_depth = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)