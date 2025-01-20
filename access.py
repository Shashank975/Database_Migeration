import pyodbc
import json
from datetime import datetime
from pymongo import MongoClient
from urllib.parse import quote_plus



def migerate_to_mongodb():
    try:
        username = quote_plus('shashank')
        password = quote_plus('123@abc')
        uri = f'mongodb+srv://{username}:{password}@advwork.mmbzc.mongodb.net/?retryWrites=true&w=majority&appName=AdvWork'
        client = MongoClient(uri)
        print("Connected successfully")
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        return None

if __name__ == "__main__":
    migerate_to_mongodb()