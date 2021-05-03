from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, insert, delete
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contrasena = db.Column(db.String(80), unique=False, nullable=False)
    #tipo = db.Column(db.Integer, ForeignKey('tiposusuario.guid'), unique=False, nullable=False)
    activo = db.Column(db.Boolean(), unique=False, nullable=False)
    #TiposUsuario = relationship(TiposUsuario)

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
