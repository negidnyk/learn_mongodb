from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from config import DB_USER, DB_PASS

# user = {
#     "_id": 1,
#     "first_name": "Mike",
#     "second_name": "Johnson",
#     "bio": "Hello, world!",
#     "created_at": datetime.datetime.now(tz=datetime.timezone.utc),
# }
#
# user2 = {
#     "_id": 1,
#     "first_name": "Mike",
#     "second_name": "Johnson",
#     "bio": "Hello, world!",
#     "created_at": datetime.datetime.now(tz=datetime.timezone.utc),
# }

uri = f"mongodb+srv://{DB_USER}:{DB_PASS}@cluster0.rd276wj.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test_db

users_collection = db.users



# def insert_smth(some_dict):
#     checkpoint = True
#     counter = 1
#     while checkpoint is True:
#         if collection.count_documents({"_id": counter}) == 0:
#             some_dict["_id"] = counter
#             collection.insert_one(some_dict)
#             checkpoint = False
#         else:
#             counter += 1


# insert_smth(user2)

# bio = collection.find_one({"_id": 1})["bio"]
# one_user = collection.find_one({"_id": 1})
# users_list = collection.find()
# print(bio)
# print(one_user)
# for user in users_list:
#     print(user)
