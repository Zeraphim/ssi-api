import mysql.connector
# import  pymysql
import os
import time





#this is a comment
#this is a test
#test comment Gabriel Deveraturda

# Connection parameters
# host = 'localhost'
# user = 'ssiadmin'
# password = 'root321'
# database = 'mysql'

host = "ssi-mariadb-test.mariadb.database.azure.com"
user = "ssi@ssi-mariadb-test"
password = "adminTest1"
database = "ssi"


# cnx = mysql.connector.connect(user="ssi@ssi-mariadb-test", password="adminTest1", host="ssi-mariadb-test.mariadb.database.azure.com", port=3306, database={your_database}, ssl_ca={ca-cert filename}, ssl_verify_cert=true)

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


        while True:
            os.system('clear')

            print(f"\n> {'='*9} S S I  D B {'='*9} <\n\n1: Show All Databases\n2: Show Tables \n3. Run Command\n4. Pic Upload\n5: Exit\n")
            response = input("> ")

            if response == "1":

                print('\n')

                # Show all databases
                show_databases_sql = "SHOW DATABASES;"
                cursor.execute(show_databases_sql)
                databases = cursor.fetchall()
                
                for db in databases:
                    print(db[0])

                input('\nPaused enter any key: ')

            elif response == "2":

                print('\n')

                # Show all tables
                show_databases_sql = "SHOW TABLES;"
                cursor.execute(show_databases_sql)
                databases = cursor.fetchall()
                
                for db in databases:
                    print(db[0])

                input('\nPaused enter any key: ')

            elif response == "3":
                q = input("\nEnter Querry: ")

                cursor.execute(q)

                rows = cursor.fetchall()

                for row in rows:
                    print(row)

                input('\nPaused enter any key: ')

            elif response == "4":
                photo_path = "/Users/zeraphim/Desktop/a.png"
                
                with open(photo_path, "rb") as photo_file:
                    photo_data = photo_file.read()

                q = f"INSERT INTO Projects (name, description, photo, category) VALUES ('Project A', 'This is a description', {photo_data}, 1)"

                
            elif response == "5":
                break

            else:
                print("\n**Invalid response**\n")
                time.sleep(1)
                input('\nPaused enter any key: ')
                continue

        # cursor.execute("CREATE TABLE Category (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),description VARCHAR(255));")

        # cursor.execute("INSERT INTO Category (name, description) VALUES ('Category 1', 'This is a description');")
        # cursor.execute("INSERT INTO Category (name, description) VALUES ('Category 2', 'This is a description');")
        # cursor.execute("INSERT INTO Category (name, description) VALUES ('Category 3', 'This is a description');")

        # cursor.execute("SELECT * FROM CATEGORY;")
    
        # rows = cursor.fetchall()
        
        # for row in rows:
        #     print(row)

        # Drop Table
        # cursor.execute("DROP TABLE category;")
        # databases = cursor.fetchall()
        
        # for db in databases:
        #     print(db[0])


        # cursor.execute("CREATE TABLE Projects (name VARCHAR(255), description TEXT, link VARCHAR(255), category VARCHAR(255));")
        # databases = cursor.fetchall()
        
        # for db in databases:
        #     print(db[0])

        # Show Tables
        # cursor.execute("SHOW TABLES;")
        # databases = cursor.fetchall()
        # for db in databases:
        #     print(db[0])


    

except mysql.connector.Error as error:
    print("Error: {}".format(error))

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.commit()
        connection.close()
        print("MySQL connection is closed.")
