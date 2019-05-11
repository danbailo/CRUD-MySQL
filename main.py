#data for example
#https://github.com/datacharmer/test_db

#CRUD in SQL
#Create           - INSERT
#Read (Retrieve)  - SELECT
#Update (Modify)  -	UPDATE
#Delete (Destroy) - DELETE


import mysql.connector
import datetime
from mysql.connector import errorcode

def connect(user=None, password=None, host=None, database=None):
    if user is None or password is None: return False
    if host and database: config = {'user': user,'password': password,'host': host,'database': database}
    elif host: config = {'user': user, 'password': password, 'host': host}
    else: config = {'user': user, 'password': password}
    # print(config)
    # print(len(config))
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        print(err)

def connect_database(cursor, database_name):
    try:
        cursor.execute("USE {}".format(database_name))
    except mysql.connector.Error as err:
        print(err)
        exit(1)        

def create_database(cursor, database_name):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def drop_database(cursor, database_name):
    try:
        cursor.execute("DROP DATABASE {}".format(database_name))
    except mysql.connector.Error as err:
        print("Failed delete database: {}".format(err))
        exit(1)

def close(connector,cursor):
    cursor.close()
    connector.close()

def query(cursor):
    cursor.execute("SELECT NOW()")
    for x in cursor:
        print(x)

connector = connect('daniel','123456789')
if connector: cursor = connector.cursor()
else: 
    print('error')
    exit(1)

connect_database(cursor, 'employees')

query(cursor)

# query = ("SELECT first_name, last_name, hire_date FROM employees "
# "WHERE hire_date BETWEEN %s AND %s")

# hire_start = datetime.date(1999, 1, 1)
# hire_end = datetime.date(1999, 12, 31)

# cursor.execute(query, (hire_start, hire_end))

# for (first_name, last_name, hire_date) in cursor:
#     print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))


close(connector, cursor)
