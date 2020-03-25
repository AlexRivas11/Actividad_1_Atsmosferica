# Consultas en MongoDB

import pymongo


def mongo_connect():
    uri_mongo = "" # TO-DO: Poner vuestra cadena de conexión de MongoDB Atlas
    client = pymongo.MongoClient(uri_mongo)
    client.test
    return client


def get_stations(collection):
    data = collection.find({'intensidad': "180"})
    for i in data:
         print(i)
    return data


if __name__ == "__main__":
    print("Start script...")
    # Parameters
    db = "" #TO-DO: poner nombre de bbdd
    col = "" # TO-DO: poner nombre colección

    # Functions
    cli_mong = mongo_connect()

    db_m = cli_mong[db]
    col_m = db_m[col]

    # get data
    stations = get_stations(col_m)

    print("Finish...")

