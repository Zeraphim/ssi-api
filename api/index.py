# How to use
# http://127.0.0.1:5000/api/hello

from flask import Flask
import mysql.connector

# app = Flask(__name__)

# @app.route('/api/hello', methods=['GET'])
# def hello_world():
#     return "Hello, World!"

# # main driver function
# if __name__ == '__main__':

#     app.run()

host = "ssi-mariadb-test.mariadb.database.azure.com"
user = "ssi@ssi-mariadb-test"
password = "adminTest1"
database = "mysql"


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

        # Show all databases
        show_databases_sql = "SHOW DATABASES;"
        cursor.execute(show_databases_sql)
        databases = cursor.fetchall()
        
        print("List of databases:")
        for db in databases:
            print(db[0])
    

except mysql.connector.Error as error:
    print("Error: {}".format(error))

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")


app = Flask(__name__)

@app.route('/')
def home():
    return 'SSI API'

@app.route('/GetAllProjects')
def about():
    return 'About'