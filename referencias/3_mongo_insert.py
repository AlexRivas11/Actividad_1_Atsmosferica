# Insertar datos en MongoDB

import pymongo
import csv


def mongo_connect():
    # uri_mongo = "" # TO-DO: Poner vuestra cadena de conexión de MongoDB Atlas
    client = pymongo.MongoClient(uri_mongo)
    client.test
    return client


def read_csv(csv_path):
    # create list of dictionaries
    ls_rows = []
    file = open(csv_path, mode='r')

    ls_csv = csv.DictReader(file, delimiter=';')
    for i in ls_csv:
        dct_row = dict(i)
        ls_rows.append(dct_row)
    file.close()
    return ls_rows


def insert_mongo_list(list_data, mongo_client, database, collection):
    # first define the collection to insert
    db = mongo_client[database]
    col = db[collection]
    for i in list_data:
        # insert one to one
        col.insert_one(i)


if __name__ == "__main__":
    # Parameters
    #db_name = "" #TO-DO: poner nombre de bbdd
    #collection_name = "" # TO-DO: poner nombre colección
    #csv_file = '' # TO-DO: poner nombre del fichero csv (alojado el en proyecto)

    # mongoDB connection
    cli = mongo_connect()
    ls_csv = read_csv(csv_path=csv_file)
    insert_mongo_list(list_data=ls_csv, mongo_client=cli, database=db_name, collection=collection_name)
