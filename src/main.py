#data for example
#https://github.com/datacharmer/test_db
#https://medium.com/@ramojol/python-context-managers-and-the-with-statement-8f53d4d9f87


#CRUD in SQL
#Create           - INSERT
#Read (Retrieve)  - SELECT
#Update (Modify)  -	UPDATE
#Delete (Destroy) - DELETE
from core import MySQLcompatible
import utils

if __name__ == "__main__":
    with MySQLcompatible('daniel','123456789',) as db:
        utils.show_databases(db)
        utils.connect_database(db,'TRABALHO_BD1')
        utils.query(db, 'select * from ENDERECO')
