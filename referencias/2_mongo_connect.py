# TO-DO: Instalar previamente los paquetes pymongo y dnspython

import pymongo

def mongo_connect():
    uri_mongo = "" # TO-DO: Poner vuestra cadena de conexión de MongoDB Atlas
    client = pymongo.MongoClient(uri_mongo)
    db = client.test
    ls_dbs = client.list_database_names()
    for db in ls_dbs:
        print(db)


if __name__ == "__main__":
    print("Hello, I'm using Python...")
    client = None
    mongo_connect()
    print("Finish script...")

