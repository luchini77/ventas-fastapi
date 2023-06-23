from config.base_datos import base
from sqlalchemy import Column, Integer, String


class Ventas(base):
    __tablename__='ventas'
    id = Column(Integer, primary_key=True)
    fecha = Column(String)
    producto = Column(String)
    valor = Column(Integer)