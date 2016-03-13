import os
from bottle import *
from bottle import request as req
import json

# local import
from qr_code_dementia import *

@route('/')
def index(section='home'):
    return template('index')

@error(404)
def error404(error):
    return 'This is not the page you are looking for.'

@get('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='static')
    
@get('/bower_components/<filepath:path>')
def bower_files(filepath):
    return static_file(filepath, root='bower_components')

@post('/make-qr')
def make_qr():
	name = str(req.POST.get('name'))
	emergency_contact = str(req.POST.get('emergencyContact'))

	generate(name, emergency_contact)
	save_in_db(name, emergency_contact)

	return json.dumps({
		'res' : [name, emergency_contact]
		})

@get('/goto-make-qr')
def goto_make_qr():
	return template('make_qr')

@get('/')
def index():
	return template('index')

@get('/<query>')
def get_info(query):

	query = query.split(".")	

	name = str(query[0])
	emergency_contact = str(query[1])

	print 'emergency_contact'
	print emergency_contact
	print 'name'
	print name

	atuk = get_atuk(name, emergency_contact)
	if atuk==None:
		return template('get_info', name=None, contact=None)
	try:
		del atuk['_id']
	except KeyError:
		pass

	return template('get_info', name=name, contact=emergency_contact)
	# return json.dumps(atuk)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 1337))
    run(host='0.0.0.0', port=port, debug=True, reloader=True)