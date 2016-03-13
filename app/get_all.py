from pymongo import MongoClient
from auth import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.get_default_database()
dementia = db['dementia']

if __name__=="__main__":
	atuks = dementia.find({})
	for atuk in atuks:
		print atuk