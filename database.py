from pymongo import MongoClient

client = MongoClient("mongodb+srv://bello:bello123@cluster0.k4ehg.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.filed_test


