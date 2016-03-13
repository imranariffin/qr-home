import qrcode
from pymongo import MongoClient
from auth import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.get_default_database()
dementia = db['dementia']

def generate(name, contact):

	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_M,
		box_size=10,
		border=4,
		)
	strinput = "localhost:1337/" + name + "." + contact

	qr.add_data(strinput)
	img = qr.make_image()
	directory = "../static/img/"
	img.save(directory + name + contact + ".jpg")

def save_in_db(name, contact):
	url = "../static/img/" + name + contact + ".jpg"
	dementia.insert_one({
		'name' : name,
		'contact' : contact
		})

def get_atuk(name, contact):
	atuk = dementia.find_one({
		'name' : name,
		'contact' : contact
		})
	print atuk
	return atuk

if __name__=="__main__":
	# save_in_db("imranyo", "01213")	
	print get_atuk("imran", "yooo")
	# generate("imran", "yooo")