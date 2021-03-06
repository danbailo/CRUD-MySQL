import mysql.connector
from mysql.connector import errorcode

def show_databases(cursor):
	try:
		print('Databases existing:')
		cursor.execute('SHOW DATABASES')
		for line in cursor:
			print(line[0])		
	except Exception as err:
		print('ERROR!: {}'.format(err))

def connect_database(cursor, database_name):
	try:
		if is_connected(cursor):
			print('\nYou are already connected in to the database!\n')
			return None
		cursor.execute('USE {}'.format(database_name))
		print('\nSuccessfully Connected with {}!\n'.format(database_name))
	except Exception as err:
		print('ERROR!: {}'.format(err))        

def create_database(cursor, database_name):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
    except Exception as err:
        print('Failed creating database: {}'.format(err))

def drop_database(cursor, database_name):
    try:
        cursor.execute('DROP DATABASE {}'.format(database_name))
    except Exception as err:
        print('Failed delete database: {}'.format(err))

def query(cursor, query):
	try:
		cursor.execute(query)
		for line in cursor:
			for i in range(len(line)):
				print(line[i], end = '; ')
			print()						
	except Exception as err:
		print('ERROR!: {}'.format(err))

def is_connected(cursor):
	cursor.execute('SELECT DATABASE()')
	for line in cursor:
		if line[0] is None: return False
		else: return True