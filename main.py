#data for example
#https://github.com/datacharmer/test_db
#https://medium.com/@ramojol/python-context-managers-and-the-with-statement-8f53d4d9f87


#CRUD in SQL
#Create           - INSERT
#Read (Retrieve)  - SELECT
#Update (Modify)  -	UPDATE
#Delete (Destroy) - DELETE

import MySQLcompatible as MySQL
from MySQLcompatible import connect_database, create_database, drop_database, query

if __name__ == "__main__":
    
    with MySQL.MySQLcompatible('daniel','123456789') as db:
        print(db)
        connect_database(db,'TRABALHO_BD1')
        query(db)
