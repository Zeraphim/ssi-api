import mysql.connector
import os
import time

#this is a comment
#this is a test
#test comment Gabriel Deveraturda

# Connection parameters
host = 'localhost'
user = 'ssiadmin'
password = 'root321'
database = 'mysql'

# connecting to mariadb
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Show all databases
        show_databases_sql = "SHOW DATABASES;"
        cursor.execute(show_databases_sql)
        databases = cursor.fetchall()
        
        print("List of databases:")
        for db in databases:
            print(db[0])

        # while True:
        #     os.system('clear')

        #     print(f"\n> {'='*9} OutSystems {'='*9} <\n\n1: GetAllPartners\n2: GetAllCareers \n3: GetAllProjects\n4. Add Inquiry\n5. Show Databases\n6. Exit\n")
        #     response = input("> ")

        #     if response == "1":


        #     elif response == "2":
        #         os.system('clear')

        #     elif response == "3":
        #         # Show all databases
        #         show_databases_sql = "SHOW DATABASES;"
        #         cursor.execute(show_databases_sql)
        #         databases = cursor.fetchall()
                
        #         print("List of databases:")
        #         for db in databases:
        #             print(db[0])

        #     elif response == "6":
        #         exit

        #     else:
        #         print("\n**Invalid response**\n")
        #         time.sleep(1)
        #         os.system('clear')
        #         continue
    

except mysql.connector.Error as error:
    print("Error: {}".format(error))

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
