from qrcode import *

def generate(name, contact):

	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_M,
		box_size=10,
		border=4,
		)

	strinput = "localhost:1337/" + name + contact

	qr.add_data(strinput)
	img = qr.make_image()
	im.save(name + contact + ".jpg")

def read(query):
	'lalala'

