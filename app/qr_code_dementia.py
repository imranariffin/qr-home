import os
import qrcode
from pymongo import MongoClient
try:
	from auth import MONGOLAB_URI
except:
	MONGOLAB_URI = os.environ.get('MONGOLAB_URI')

client = MongoClient(MONGOLAB_URI)
db = client.get_default_database()
dementia = db['dementia']

def generate(name, contact):

	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_M,
		box_size=10,
		border=4,
		)
	# strinput = "localhost:1337/" + name + "." + contact
	strinput = "http://qr-home.herokuapp.com/" + name + "." + contact
	directory = "../static/img/"

	print "do not use localhost!"
	print "saved at:"
	print directory + name + contact + ".jpg"

	qr.add_data(strinput)
	img = qr.make_image()
	img.save(name + contact + ".jpg")
	os.system("cp ./" + name + contact + ".jpg" + " ./static/img/")	

def save_in_db(name, contact):
	url = "../static/img/" + name + contact + ".jpg"

	check = dementia.find_one({
		'name' : name
		})

	if check==None:
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