from pymongo import MongoClient
from auth import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.get_default_database()
dementia = db['dementia']

if __name__=="__main__":


	seed = [
	{
		'name' : 'imranariffin',
		'contact' : '0123456789'
	},
	{
		'name' : 'hanifariffin',
		'contact' : '987654321'
	}
	]

	dementia.insert(seed)