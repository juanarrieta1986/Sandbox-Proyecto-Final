from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, insert, delete
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(80), unique=False, nullable=False)
    tipo = db.Column(db.Integer, ForeignKey('tiposusuario.guid'), unique=False, nullable=False)
    activo = db.Column(db.Boolean(), unique=False, nullable=False)
    TiposUsuario = relationship(TiposUsuario)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "tipo": self.tipo,
            "activo": self.activo,
            # do not serialize the password, its a security breach
        }

class TiposUsuario(db.Model):
    __tablename__ = 'tiposusuario'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(120), unique=True, nullable=False)
    guid = db.Column(db.String(120), unique=True, nullable=False)
    #User = relationship(User)

    def serialize(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            # do not serialize the password, its a security breach
        }

class Provincias(db.Model):
    __tablename__ = 'provincias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            # do not serialize the password, its a security breach
        }
    
class Cantones(db.Model):
    __tablename__ = 'cantones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    provincias = db.Column(db.Integer, ForeignKey('provincias.id'), nullable=True)
    #provincia = db.Column(db.Integer, ForeignKey('provincias.id'), nullable=True)
    Provincias = relationship(Provincias)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "provincia": self.provincia,
            # do not serialize the password, its a security breach
        }

class TiposServicio(db.Model):
    __tablename__ = 'tiposServicio'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            # do not serialize the password, its a security breach
        }

class Pyme(db.Model):
    __tablename__ = 'pyme'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), unique=True, nullable=False)
    provincia = db.Column(db.Integer, ForeignKey('provincias.id'), unique=False, nullable=False)
    canton = db.Column(db.Integer, ForeignKey('cantones.id'), unique=False, nullable=False)
    otrassenas = db.Column(db.String(80), unique=False, nullable=False)
    servicio = db.Column(db.String(80), unique=False, nullable=False)
    telefono = db.Column(db.String(80), unique=False, nullable=False)
    facebook = db.Column(db.String(80), unique=False, nullable=False)
    instragram = db.Column(db.String(80), unique=False, nullable=False)
    Provincias = relationship(Provincias)
    Cantones = relationship(Cantones)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "provincia": self.provincia,
            "canton": self.canton,
            "otrasenas": self.otrasenas,
            "servicio": self.servicio,
            "telefono": self.telefono,
            "facebook": self.facebook,
            "instragram": self.instragram,
            # do not serialize the password, its a security breach
        }