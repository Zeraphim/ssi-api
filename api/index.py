# How to use
# http://127.0.0.1:5000/api/hello

from flask import Flask
import mysql.connector
import json

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
database = "ssi"


# cnx = mysql.connector.connect(user="ssi@ssi-mariadb-test", password="adminTest1", host="ssi-mariadb-test.mariadb.database.azure.com", port=3306, database={your_database}, ssl_ca={ca-cert filename}, ssl_verify_cert=true)


app = Flask(__name__)

@app.route('/')
def home():
    return 'SSI API\n\nCommands:\n1. GetAllDepartments\n2./GetAllCategories'

@app.route('/GetAllProjects')
def about():
    return 'About'

@app.route('/GetAllDepartments')
def departments():

    # connecting to mariadb
    try:

        return_dict = {}
        cols = ['id', 'name']

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()

            show_databases_sql = "SELECT * FROM DEPARTMENT;"
            cursor.execute(show_databases_sql)
            department_data = cursor.fetchall()
        
            department_list = []
            for row in department_data:
                department_dict = {
                    "id": row[0],
                    "name": row[1]
                }
                department_list.append(department_dict)

            # Convert the list of dictionaries to JSON
            department_json = json.dumps(department_list, indent=4)

            return department_json
        

    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Departments'



@app.route('/GetAllCategories')
def categories():

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

            show_databases_sql = "SELECT * FROM CATEGORY;"
            cursor.execute(show_databases_sql)
            category_data = cursor.fetchall()
        
            category_list = []
            for row in category_data:
                category_dict = {
                    "id": row[0],
                    "name": row[1],
                    "description": row[2]
                }
                category_list.append(category_dict)

            # Convert the list of dictionaries to JSON
            category_json = json.dumps(category_list, indent=4)

            return category_json
        

    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Departments'