# app.py

from flask import Flask, request, jsonify
from config import Config
from models import db, Persona, Producto, Factura  # Importar las clases del modelo

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar SQLAlchemy con la aplicación Flask
db.init_app(app)

# Crear las tablas en la base de datos (si no existen)
with app.app_context():
    db.create_all()

@app.route('/api/facturacion', methods=['POST'])
def crear_facturacion():
    try:
        data = request.json
        
        # Asegurarse de que los datos se reciban correctamente
        if not data:
            return jsonify({'error': 'No se recibieron datos en el request'}), 400
        
        # Crear la persona
        persona_data = data.get('persona')
        if not persona_data:
            return jsonify({'error': 'Faltan datos de persona'}), 400

        persona = Persona(
            nombre=persona_data.get('nombre'),
            direccion=persona_data.get('direccion'),
            rfc=persona_data.get('rfc'),
            edad=persona_data.get('edad'),
            regimen=persona_data.get('regimen')
        )
        db.session.add(persona)
        db.session.commit()  # Guardar los cambios y obtener el ID de la persona

        # Crear el producto
        producto_data = data.get('producto')
        if not producto_data:
            return jsonify({'error': 'Faltan datos de producto'}), 400

        producto = Producto(
            nombre=producto_data.get('nombre'),
            cantidad=producto_data.get('cantidad'),
            precio=producto_data.get('precio'),
            sku=producto_data.get('sku')
        )
        db.session.add(producto)
        db.session.commit()  # Guardar los cambios y obtener el ID del producto

        # Crear la factura
        factura_data = data.get('factura')
        if not factura_data:
            return jsonify({'error': 'Faltan datos de factura'}), 400

        total = producto.precio * factura_data.get('cantidad')
        factura = Factura(
            id_producto=producto.id_producto,
            id_persona=persona.id_persona,
            cantidad=factura_data.get('cantidad'),
            total=total
        )
        db.session.add(factura)
        db.session.commit()  # Guardar la factura

        # Responder con los IDs generados
        return jsonify({
            'id_persona': persona.id_persona,
            'id_producto': producto.id_producto,
            'id_factura': factura.id_factura,
            'total': float(total)
        }), 201

    except Exception as e:
        # Captura el error y devuelve un mensaje con el detalle del mismo
        return jsonify({'error': str(e)}), 500

