from config.base_datos import base
from sqlalchemy import Column,Integer,String

#modelos
class Usuario(base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    clave = Column(String)