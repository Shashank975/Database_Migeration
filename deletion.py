#deletion_steps =
from urllib.parse import quote_plus
from pymongo import MongoClient

def delete_all_collections():
    try:
        # MongoDB connection details
        username = quote_plus('shashank')
        password = quote_plus('123@abc')
        uri = f'mongodb+srv://{username}:{password}@advwork.mmbzc.mongodb.net/?retryWrites=true&w=majority&appName=AdvWork'
        
        # Connect to MongoDB
        client = MongoClient(uri)
        print("Connected successfully")
        db = client["AdventureWorks"]  # Using AdventureWorks database

        # List all collections
        collections = db.list_collection_names()
        print(f"Found {len(collections)} collections to delete.")

        # Delete each collection
        for collection_name in collections:
            try:
                db.drop_collection(collection_name)
                print(f"Collection {collection_name} deleted successfully.")
            except Exception as e:
                print(f"Error deleting collection {collection_name}: {e}")

    except Exception as e:
        print("Error connecting to MongoDB:", e)


# Call the delete function
if __name__ == "__main__":
    delete_all_collections()