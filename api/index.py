# How to use
# http://127.0.0.1:5000/api/hello

from flask import Flask, jsonify
import mysql.connector
import json

'''

Missing:

1. GetAllInquiry - Kyle
2. GetAllPartner - Kyle
3. GetAllService - Gab
4. GetAllProject - Bryan
5. GetAllOpportunity - Bryan

'''

host = "ssi-mariadb-test.mariadb.database.azure.com"
user = "ssi@ssi-mariadb-test"
password = "adminTest1"
database = "ssi"


# cnx = mysql.connector.connect(user="ssi@ssi-mariadb-test", password="adminTest1", host="ssi-mariadb-test.mariadb.database.azure.com", port=3306, database={your_database}, ssl_ca={ca-cert filename}, ssl_verify_cert=true)


app = Flask(__name__)


@app.route('/')
def home():

    data = {
        "title": "This is a proof-of-concept API server. You can test each endpoint by creating a GET request for each one. The data they return is EXACTLY the same data that the frontend will expect.",
        "endpoints": [
            {
                "url": "/getWebsiteData",
                "params": [],
                "method": "GET",
                "description": "Returns a list of Service Categories and Projects that are displayed on the website.",
                "example_request": "/getWebsiteData"
            },
            {
                "url": "/getAllProjects",
                "params": [
                    {
                        "name": "id",
                        "type": "int",
                        "required": "true"
                    },
                    {
                        "name": "name",
                        "type": "string",
                        "required": "true"
                    },
                    {
                        "name": "category",
                        "type": "string",
                        "required": "true"
                    },
                    {
                        "name": "description",
                        "type": "string",
                        "required": "true"
                    }
                ],
                "method": "GET",
                "description": "Returns a list of Projects.",
                "example_request": "/getProjects"
            },
            {
                "url": "/getAllOpportunity",
                "params": [
                    {
                        "name": "department",
                        "type": "string",
                        "required": "true",
                    },
                    {
                        "name": "experience_level",
                        "type": "string",
                        "required": "true"
                    }
                ],
                "method": "GET",
                "description": "Returns a list of Opportunity that fulfills the Department and Experience Level filters.",
                "example_request": "/getOpportunities?department=Engineering&experience_level=Internship"
            },
            {
                "url": "/getOpportunity",
                "params": [
                    {
                        "name": "id",
                        "type": "int",
                        "required": "true"
                    }
                ],
                "method": "GET",
                "description": "Returns an Opportunity with the same id.",
                "example_request": "/getOpportunity?id=1"
            },
            {
                "url": "/getAllDepartments",
                "params": [
                    {
                        "name": "id",
                        "type": "int",
                        "required": "true"
                    },
                    {
                        "name": "name",
                        "type": "string",
                        "required": "true"
                    }
                ],
                "method": "GET",
                "description": "Returns a list of Projects.",
                "example_request": "/getProjects"
            },
            {
                "url": "/getAllProjects",
                "params": [
                    {
                        "name": "id",
                        "type": "int",
                        "required": "true"
                    },
                    {
                        "name": "name",
                        "type": "string",
                        "required": "true"
                    },
                    {
                        "name": "category",
                        "type": "string",
                        "required": "true"
                    },
                    {
                        "name": "description",
                        "type": "string",
                        "required": "true"
                    }
                ],
                "method": "GET",
                "description": "Returns a list of Projects.",
                "example_request": "/getProjects"
            },
            {
                "url": "/getAllService",
                "params": [
                    {
                        "name": "id",
                        "type": "int",
                        "required": "true"
                    },
                    {
                        "name": "name",
                        "type": "string",
                        "required": "true"
                    },
                    {
                        "name": "description",
                        "type": "string",
                        "required": "true"
                    }
                ],
                "method": "GET",
                "description": "Returns a list of Projects.",
                "example_request": "/getAllService"
            },
            {
                "url": "/getAllCategories",
                "params": [
                    {
                        "name": "id",
                        "type": "int",
                        "required": "true"
                    },
                    {
                        "name": "name",
                        "type": "string",
                        "required": "true"
                    },
                    {
                        "name": "description",
                        "type": "string",
                        "required": "true"
                    }
                ],
                "method": "GET",
                "description": "Returns a list of Categories.",
                "example_request": "/getAllCategories"
            },
        ]
    }

    # return 'SSI API\n\nCommands:\n1. GetAllDepartments\n2./GetAllCategories'
    return (data)


@app.route('/getWebsiteData')
def websiteData():

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

            # Create a dictionary to store the results
            all_dict = {'Departments': []}
            for row in department_data:
                department = {
                    'id': row[0],
                    'name': row[1]
                }
                all_dict['Departments'].append(department)

            # Convert the dictionary to a JSON object
            all_json = json.dumps(all_dict, indent=4)

            return all_json

    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Departments'


@app.route('/GetAllProjects')
def projects():
    # connecting to mariadb
    try:

        return_dict = {}
        cols = ['id', 'name', 'category', 'description']

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()

            show_databases_sql = "SELECT * FROM PROJECTS;"
            cursor.execute(show_databases_sql)
            project_data = cursor.fetchall()

            project_list = []
            for row in project_data:
                project_dict = {
                    "id": row[0],
                    "name": row[1],
                    "category": row[2],
                    "description": row[3]
                }
                project_list.append(project_dict)

            # Convert the list of dictionaries to JSON
            project_json = json.dumps(project_list, indent=4)

            return project_json

    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Projects'


@app.route('/GetAllOpportunity')
def opportunity():
    # connecting to mariadb
    try:

        return_dict = {}
        cols = ['ID', 'title', 'location', 'department',
                'experience_level', 'description']

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()

            show_databases_sql = "SELECT * FROM OPPORTUNITIES;"
            cursor.execute(show_databases_sql)
            opportunity_data = cursor.fetchall()

            opportunity_list = []
            for row in opportunity_data:
                opportunity_dict = {
                    "ID": row[0],
                    "title": row[1],
                    "location": row[2],
                    "department": row[3],
                    "experience_level": row[4],
                    "description": row[5]
                }
                opportunity_list.append(opportunity_dict)

            # Convert the list of dictionaries to JSON
            project_json = json.dumps(opportunity_list, indent=4)

            return project_json

    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Opportunities'


@app.route('/getAllService')
def services():

    # connecting to mariadb
    try:

        return_dict = {}
        cols = ['id', 'name', 'description']

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()

            show_services_sql = "SELECT * FROM SERVICES;"
            cursor.execute(show_services_sql)
            service_data = cursor.fetchall()

            service_list = []
            for row in service_data:
                service_dict = {
                    "id": row[0],
                    "name": row[1],
                    "description": row[2]
                }
                service_list.append(service_dict)

            # Convert the list of dictionaries to JSON
            service_json = json.dumps(service_list, indent=4)

            return service_json

    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Services'


@app.route('/getAllDepartments')
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

            # Create a dictionary to store the results
            departments_dict = []
            for row in department_data:
                department = {
                    'id': row[0],
                    'name': row[1]
                }
                departments_dict.append(department)

            # Convert the dictionary to a JSON object

            return jsonify(departments_dict)

    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Departments'


@app.route('/getAllCategories')
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

    return 'Categories'


@app.route('/AddInquiry')
def AddInquiry():

    return 'Add Inquiry'
    # outsystems


# comment this out when running in vercel
app.run()
