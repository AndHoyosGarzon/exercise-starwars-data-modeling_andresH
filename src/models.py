import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fecha_de_suscripcion = Column(Date, nullable=False)
    password = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)

class Login(Base):
    __tablename__ = 'login'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fecha_login = Column(Date, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))



class Personajes(Base):
    __tablename__= 'personaje'
    id = Column(Integer, primary_key=True)
    color_de_ojos = Column(String(250), nullable=False)
    color_de_cabello = Column(String(250), nullable=False)
    login_id = Column(Integer, ForeignKey('login.id'))

class Planetas(Base):
    __tablename__= 'planeta'
    id = Column(Integer, primary_key=True)
    terreno = Column(String(250), nullable=False)
    poblacion = Column(String(250), nullable=False)
    login_id = Column(Integer, ForeignKey('login.id'))

class vehiculos(Base):
    __tablename__= 'vehiculo'
    id = Column(Integer, primary_key=True)
    llantas = Column(String(250), nullable=False)
    capacidad = Column(String(250), nullable=False)
    puertas = Column(String(250), nullable=False)
    login_id = Column(Integer, ForeignKey('login.id'))

class Favoritos(Base):
    __tablename__= 'favoritos'
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    vehiculo_id = Column(Integer, ForeignKey('vehiculo.id'))
    login_id = Column(Integer, ForeignKey('login.id'))
##agregar tabla favoritos por entidas y tabla favoritos por todos














    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
