import mysql.connector
# import  pymysql
import os
import time


# this is a comment
# this is a test
# test comment Gabriel Deveraturda
# inserted data to services

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

def convertToBinary(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def convertBinaryToFile(binarydata, filename):
    with open(filename, 'wb') as file:
        file.write(binarydata)

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

            print(
                f"\n> {'='*9} S S I  D B {'='*9} <\n\n1: Show All Databases\n2: Show Tables \n3. Run Command\n4. Pic Upload\n5: Exit\n")
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

                q = """INSERT INTO Partners (partnerID, name, imageData) VALUES (%s, %s, %s);"""
                convertPic = convertToBinary(
                    r"C:\Users\Zeraphim\Desktop\Outsystems1.png")
                values = (2, "OutSystems", convertPic)

                cursor.execute(q, values)

            elif response == "5":
                break

            else:
                print("\n**Invalid response**\n")
                time.sleep(1)
                input('\nPaused enter any key: ')
                continue


except mysql.connector.Error as error:
    print("Error: {}".format(error))

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.commit()
        connection.close()
        print("MySQL connection is closed.")
