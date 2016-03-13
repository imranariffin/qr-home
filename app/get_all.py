import os
from pymongo import MongoClient
try:
	from auth import MONGOLAB_URI
except:
	MONGOLAB_URI = os.environ.get('MONGOLAB_URI')

client = MongoClient(MONGOLAB_URI)
db = client.get_default_database()
dementia = db['dementia']

if __name__=="__main__":
	atuks = dementia.find({})
	for atuk in atuks:
		print atuk