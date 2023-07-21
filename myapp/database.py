from pymongo import MongoClient
def get_db_handle():
    client = MongoClient("mongodb+srv://ramansain65:6zWguNNFWwDnczap@cluster0.hqv1bnv.mongodb.net/")
    db_handle = client["srib"]
    return db_handle, client

def get_collection_handle(db_handle,collection_name):
    return db_handle[collection_name]


