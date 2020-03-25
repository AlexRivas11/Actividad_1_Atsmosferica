# TO-DO: Instalar previamente los paquetes pymongo y pprint
import pymongo
import pprint


if __name__ == '__main__':
    print(pymongo.version)

    client = pymongo.MongoClient(" ") # TO-DO: Poner vuestra cadena de conexión de MongoDB Atlas
    # Recordar sustituir <usuario> y <password> por usuario y password del usuario de base de datos creado

    #Obtener bbdd
    db = client.bbdd_prueba

    # Obtener coleccion
    coleccion = db.coleccion

    # Crear e insertar un documento

    persona = {
         "name": "Pepe",
         "edad": 28,
         "trabajo": "Informatico",
         "opciones": ["casa1", "garaje1", "garaje2"],
         "vistas": 12
    }

    coleccion.insert_one(persona)

    # Buscar un documento
    pprint.pprint(coleccion.find_one())
    print(coleccion.find_one())

    # Buscar un documento en concreto
    pprint.pprint(coleccion.find_one({"vistas": 13}))

    # Obtener todos los documentos de una coleccion
    for documento in coleccion.find():
         pprint.pprint(documento)

    # Obtener todos los documentos de una coleccion ajustando búsqueda
    for documento in coleccion.find({"vistas": 12}):
         pprint.pprint(documento)

    # Contar número de documentos
    numero = coleccion.count_documents({})
    print("Número de documentos " + str(numero))

    coleccion.count_documents({"vistas": 12})
    print("Número de documentos " + str(numero))
