#install pymongo: python3 -m pip install pymongo

#Parametros para la creacion y conexion con la base de datos
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
 
# conexión
client = MongoClient('localhost',27017)
db = client.hacking_db

if __name__ == '__main__':
	coleccion = db.productos
	test_dicc = {"AB":55,"CD":25, "EF":20}
	coleccion.insert_one(test_dicc)
