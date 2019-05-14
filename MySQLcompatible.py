import mysql.connector
from mysql.connector import errorcode

class MySQL(object):
    """MySQL databate connection compatible with statement"""
    def __init__(self, user=None, password=None, host=None, database=None, port=None):
        if host is None: host = 'localhost'
        if port is None: port = 3306
        if user is None or password is None: return False
        
        config = {'user': user,'password': password,'host': host,'database': database, 'port': port}
        try:
            cnx = mysql.connector.connect(**config)
            return cnx
        except mysql.connector.Error as err:
            print('CONNECT ERROR -',err)
            return exit(-1)

    # def connect_database(cursor, database_name):
    #     try:
    #         cursor.execute("USE {}".format(database_name))
    #     except mysql.connector.Error as err:
    #         print(err)
    #         exit(1)        

    # def create_database(cursor, database_name):
    #     try:
    #         cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
    #     except mysql.connector.Error as err:
    #         print("Failed creating database: {}".format(err))
    #         exit(1)

    # def drop_database(cursor, database_name):
    #     try:
    #         cursor.execute("DROP DATABASE {}".format(database_name))
    #     except mysql.connector.Error as err:
    #         print("Failed delete database: {}".format(err))
    #         exit(1)

    # def close(connector,cursor):
    #     cursor.close()
    #     connector.close()

    # def query(cursor):
    #     cursor.execute("SELECT NOW()")
    #     for x in cursor:
    #         print(x)