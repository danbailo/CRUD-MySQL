#data for example
#https://github.com/datacharmer/test_db
#https://medium.com/@ramojol/python-context-managers-and-the-with-statement-8f53d4d9f87

#CRUD in SQL
#Create           - INSERT
#Read (Retrieve)  - SELECT
#Update (Modify)  -	UPDATE
#Delete (Destroy) - DELETE

import MySQLcompatible as MySQL

if __name__ == "__main__":
    
    with MySQL.MySQLcompatible('daniel','123456789').connect as db:
        print(db)

    # connector = connect('daniel','123456789','127.0.0.1',None,3306)
    # if connector: cursor = connector.cursor()
    # else: 
    #     print('error')
    #     exit(1)

    # print(connector)

    # close(connector, cursor)
