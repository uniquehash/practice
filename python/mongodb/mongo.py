from pymongo import MongoClient
import json


client = MongoClient()

db = client.test

coll = db.restaurants

items = coll.find().limit(1)
#_id = ObjectId('564223e530922c4ac2864dfe')
#item = coll.find_one({"_id": "564223e530922c4ac2864dfe"})
#item = coll.find({"key2":"value2"})


print("------------")
#print(item)
print("------------")

for document in items:
	well = document['_id']
	#print(well)

	coll.update_one({"_id":well},{"$set":{"superKey":"nooooo way"}})

items = coll.find().limit(1)


for document in items:
	print(document)
	print("------")

