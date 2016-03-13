import qrcode


entry = ""

qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_M,
	box_size=10,
	border=4,
	)

qr.add_data(entry)
img = qr.make_image()

print "I MIGHT BE LOST"
print dir(img)
print "SCAN HERE"

