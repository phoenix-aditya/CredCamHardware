from pymongo import MongoClient

db_connection_string = "mongodb+srv://aditya:aditya1234@geekstat-cluster.t9y6a2j.mongodb.net/?retryWrites=true&w=majority"

connection = MongoClient(db_connection_string)
database = connection['CredCam']

