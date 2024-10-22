import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',        # O el host de tu servidor MySQL
            user='root',       # El nombre de usuario de tu base de datos
            password='root',# La contraseña de tu base de datos
            database='ricardo'  # El nombre de la base de datos
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            # Puedes ejecutar tus consultas aquí
            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            registro = cursor.fetchone()
            print("Conectado a la base de datos: ", registro)

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == '__main__':
    conectar()

############ Insertar producto, persona y factura

def insertar_producto(nombre, cantidad, precio, sku):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO producto (nombre, cantidad, precio, sku) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre, cantidad, precio, sku))
            conexion.commit()
            print("Producto insertado correctamente.")
        except Error as e:
            print(f"Error al insertar producto: {e}")
        finally:
            cursor.close()
            conexion.close()
            
def insertar_persona(nombre, direccion, rfc, edad, regimen):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query ="INSERT INTO persona (nombre, direccion, rfc, edad, regimen) VALUES (%s, %s, %s, %s, %S)"
            cursor.execute(query, (nombre, direccion, rfc, edad, regimen))
            conexion.commit()
            print("Persona insertada correctamente.")
        except Error as e:
            print(f"Error al insertar la persona: {e}")
        finally:
            cursor.close()
            conexion.close()
            
def insertar_factura(id_producto, id_persona, fecha, cantidad, total):
    conexion = conectar()
    if conexion:
        try:
            cursor =conexion.cursor()
            query = "INSERT INTO factura(id_producto, id_persona, fecha, cantidad, total) VALUES (%s, %s, %s, %s, %s)"
            cursor. exeecute(query, (id_producto, id_persona, fecha, cantidad, total))
            conexion.comit()
            print("Factura insertada correctamente")
        except Error as e:
            print(f"Error al inserta la factura:{e}")
        finally:
            cursor.close()
            conexion.close()

#### Metodos para obtener Productos, Personas y Facturas           

def obtener_productos():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM producto")
            resultados = cursor.fetchall()
            for producto in resultados:
                print(producto)
        except Error as e:
            print(f"Error al obtener productos: {e}")
        finally:
            cursor.close()
            conexion.close()

def obtener_personas():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT*FROM persona")
            resultados= cursor.fetchall()
            for persona in resultados:
                print(persona)
        except Error as e:
            print(f"Error al obtener persona: {e}")
        finally:
            cursor.close()
            conexion.close() 
            
def obtener_factura():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT*FROM factura")
            resultados = cursor.fechall()
            for factura in resultados:
                print(factura)
        except Error as e:
            print(f"Error al obtener la factura:{e}")
        finally:
            cursor.close()
            conexion.close()  
                
####Actualizacio de Producto, Persona y Factura

def actualizar_producto(id_producto, nombre, cantidad, precio, sku):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "UPDATE producto SET nombre = %s, cantidad = %s, precio = %s, sku = %s WHERE id_producto = %s"
            cursor.execute(query, (nombre, cantidad, precio, sku, id_producto))
            conexion.commit()
            print("Producto actualizado correctamente.")
        except Error as e:
            print(f"Error al actualizar producto: {e}")
        finally:
            cursor.close()
            conexion.close()
            
def actualizar_producto(id_persona, nombre, direccion, rfc, edad, regimen):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "UPDATE persona SET nombre = %s, direccion = %s, rfc = %s, edad = %s, regimen = %s WHERE id_persona = %s"
            cursor.execute(query, ( nombre, direccion, rfc, edad, regimen), id_persona)
            conexion.commit()
            print("Persona actualizada correctamente.")
        except Error as e:
            print(f"Error al actualizar persona: {e}")
        finally:
            cursor.close()
            conexion.close()

def actualizar_factura(id_factura, id_producto, id_persona, fecha, cantidad, total):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "UPDATE factura SET id_producto = %s, id_persona = %s, fecha = %s, cantidad = %s, total =%s WHERE id_factura = %s"
            cursor.execute(query, (id_producto, id_persona, fecha, cantidad, total))
            conexion.commit()
            print("Factura actualizada correctamente.")
        except Error as e:
            print(f"Error al actualizar factura: {e}")
        finally:
            cursor.close()
            conexion.close()
            
###

def eliminar_producto(id_producto):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM producto WHERE id_producto = %s"
            cursor.execute(query, (id_producto,))
            conexion.commit()
            print("Producto eliminado correctamente.")
        except Error as e:
            print(f"Error al eliminar producto: {e}")
        finally:
            cursor.close()
            conexion.close()
            
def eliminar_persona(id_persona):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM persona WHERE id_persona = %s"
            cursor.execute(query, (id_persona,))
            conexion.commit()
            print("Persona eliminada correctamente.")
        except Error as e:
            print(f"Error al eliminar persona: {e}")
        finally:
            cursor.close()
            conexion.close()
            
def eliminar_factura(id_factura):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM factura WHERE id_factura = %s"
            cursor.execute(query, (id_factura,))
            conexion.commit()
            print("Factura eliminada correctamente.")
        except Error as e:
            print(f"Error al eliminar factura: {e}")
        finally:
            cursor.close()
            conexion.close() 