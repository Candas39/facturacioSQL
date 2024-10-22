# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Persona(db.Model):
    __tablename__ = 'persona'
    id_persona = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    rfc = db.Column(db.String(18), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    regimen = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, direccion, rfc, edad, regimen):
        self.nombre = nombre
        self.direccion = direccion
        self.rfc = rfc
        self.edad = edad
        self.regimen = regimen

class Producto(db.Model):
    __tablename__ = 'producto'
    id_producto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    sku = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre, cantidad, precio, sku):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.sku = sku

class Factura(db.Model):
    __tablename__ = 'factura'
    id_factura = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id_producto'), nullable=False)
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)

    producto = db.relationship('Producto', backref='facturas')
    persona = db.relationship('Persona', backref='facturas')

    def __init__(self, id_producto, id_persona, cantidad, total):
        self.id_producto = id_producto
        self.id_persona = id_persona
        self.fecha = db.func.current_date()
        self.cantidad = cantidad
        self.total = total
