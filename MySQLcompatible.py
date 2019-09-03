#https://docs.python.org/3/reference/datamodel.html#object.__new__

import mysql.connector
from mysql.connector import errorcode

class MySQLcompatible(object):
    """MySQL databate connection compatible with statement"""
    def __init__(self, user=None, password=None, host=None, database=None):
        if host is None: self.host = 'localhost'
        # if port is None: self.port = 3306
        if user is None or password is None: return None
        config = {'user': user,'password': password,'host': host,'database': database}
        try:
            self.connect = mysql.connector.connect(**config)
            # return self.connect
        except mysql.connector.Error as err:
            print('CONNECT ERROR -',err)
            return None

    def __enter__(self):
        self.cursor = self.connect.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connect.close()

def connect_database(cursor, database_name):
    try:
        cursor.execute('USE {}'.format(database_name))
        print('Successfully Connected!')
    except mysql.connector.Error as err:
        print(err)
        exit(1)        

def create_database(cursor, database_name):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
    except mysql.connector.Error as err:
        print('Failed creating database: {}'.format(err))
        exit(1)

def drop_database(cursor, database_name):
    try:
        cursor.execute('DROP DATABASE {}'.format(database_name))
    except mysql.connector.Error as err:
        print('Failed delete database: {}'.format(err))
        exit(1)

def query(cursor):
    cursor.execute('SELECT NOW()')
    for x in cursor:
        print(x)