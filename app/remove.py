from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.db
dementia = db.dementia

if __name__=="__main__":
	atuks = dementia.find({})
	for atuk in atuks:
		dementia.remove({'_id' : atuk['_id']})