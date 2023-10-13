# How to use
# http://127.0.0.1:5000/api/hello

from flask import Flask, request, jsonify, Response
from functools import wraps

import mysql.connector
import json
import base64
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

import traceback

from datetime import date

'''

Missing:

1. GetAllInquiry - Kyle
2. GetAllPartner - Kyle
3. GetAllService - Gab
4. GetAllProject - Bryan
5. GetAllOpportunity - Bryan

'''

host = "3.27.249.230"
user = "remoteAdmin"
password = "adminTest1"
database = "ssi"


# cnx = mysql.connector.connect(user="ssi@ssi-mariadb-test", password="adminTest1", host="ssi-mariadb-test.mariadb.database.azure.com", port=3306, database={your_database}, ssl_ca={ca-cert filename}, ssl_verify_cert=true)


app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

CORS(app)


'''

To Add:

Calendar Route

Check
schedule.svelte

'''

# Authentication

USERNAME = 'zeraphim'
PASSWORD = 'admin123'

# Check if the provided username and password are correct
def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

# Prompt the user to enter username and password
def authenticate():
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

# Decorator for checking authentication
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# Sample endpoint that requires authentication
@app.route('/api/protected')
@requires_auth
def protected():
    return 'Authentication Successful'



@app.route('/')
@requires_auth
def home():

    data = {
        "title": "This is a proof-of-concept API server. You can test each endpoint by creating a GET request for each one. The data they return is EXACTLY the same data that the frontend will expect.",
        "endpoints": [
            {
                "url": "/getWebsiteData",
                "params": [],
                "method": "GET",
                "description": "Returns all the tables in the database in JSON object format.",
                "example_request": "/getWebsiteData"
            },
            {
                "url": "/getTakenDates",
                "params": "[month, year]",
                "method": "GET",
                "description": "Return all days of the month in the year that have NO timeslots left",
                "example_request": "/getTakenDates?month=10&year=2023"
            },
            {
                "url": "/getTimeSlots",
                "params": "[day, month, year]",
                "method": "GET",
                "description": "Return all time slots available for a day",
                "example_request": "/getTimeSlots?day=15&month=10&year=2023"
            },
            {
                "url": "/addInquiry",
                "params": "[category, name, email, timeslot, date]",
                "method": "GET",
                "description": "Add an inquiry to the database",
                "example_request": "/addInquiry?category=1&name=JC%20Diamante&email=jcsd%40gmail.com&timeslot=1&date=2023-10-16"
            },
            {
                "url": "/getAllCategories",
                "params": [],
                "method": "GET",
                "description": "Returns all the categories in the database in JSON object format.",
                "example_request": "/getAllCategories"
            },
            {
                "url": "/getAllInquiries",
                "params": [],
                "method": "GET",
                "description": "Returns all the inquiries in the database in JSON object format.",
                "example_request": "/getAllInquiries"
            },
            {
                "url": "/getAllOpportunities",
                "params": [],
                "method": "GET",
                "description": "Returns all the Opportunities in the database in JSON object format.",
                "example_request": "/getAllOpportunities"
            },
            {
                "url": "/getAllPartners",
                "params": [],
                "method": "GET",
                "description": "Returns all the partners in the database in JSON object format.",
                "example_request": "/getAllPartners"
            },
            {
                "url": "/getAllProjects",
                "params": [],
                "method": "GET",
                "description": "Returns all the projects in the database in JSON object format.",
                "example_request": "/getAllProjects"
            },
            {
                "url": "/getAllTestimonials",
                "params": [],
                "method": "GET",
                "description": "Returns all the testimonials in the database in JSON object format.",
                "example_request": "/getAllTestimonials"
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
                "description": "Returns a list of Departments.",
                "example_request": "/getDepartments"
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
                "description": "Returns a list of Services.",
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
@requires_auth
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
            
            """
            
            # Fetch categories data from the "Categories" table
            cursor.execute("SELECT * FROM Categories")
            categories = cursor.fetchall()

            # Fetch other data (projects, testimonials, partners) as needed

            # Create a dictionary with the structure you want
            data = {
                "categories": [],
                "projects": [],  # Add your projects data here
                "testimonials": [],  # Add your testimonials data here
                "partners": []  # Add your partners data here
            }

            # Populate the "categories" key with the fetched data
            for category in categories:
                category_dict = {
                    'id': category[0],
                    'name': category[1],
                    'description': category[2]
                }
                data["categories"].append(category_dict)

            
            """

            # Create a dictionary to store the results
            all_dict = {
                "categories": [], # id, name, description
                "projects": [], # id, name, description, photo, category
                "testimonials": [],
                "partners": [], # partnerID, name, imageData
               }
            
            # Get Categories
            show_databases_sql = "SELECT * FROM categories;"
            cursor.execute(show_databases_sql)
            categories_data = cursor.fetchall()

            for row in categories_data:
                categories = {
                    'categoryId': row[0],
                    'name': row[1],
                    'description': row[2]
                }
                all_dict['categories'].append(categories)

            # Get Projects
            show_databases_sql = "SELECT * FROM projects;"
            cursor.execute(show_databases_sql)
            projects_data = cursor.fetchall()

            for row in projects_data:

                # photo_bytes = row[3]
                # photo_str = base64.b64encode(photo_bytes).decode('utf-8')

                projects = {
                    'id': row[0],
                    'title': row[1],
                    'category': row[2],
                    'description': row[2],
                    'photo': row[3],
                    'name': row[4],
                    'logo_url': row[5],
                    'year': row[6]
                }
                all_dict['projects'].append(projects)

            # "partners": [], # partnerID, name, imageData
            # Get Partners
            show_databases_sql = "SELECT * FROM partners;"
            cursor.execute(show_databases_sql)
            partners_data = cursor.fetchall()

            for row in partners_data:

                # photo_bytes = row[2]
                # photo_str = base64.b64encode(photo_bytes).decode('utf-8')

                partners = {
                    'partnerID': row[0],
                    'name': row[1],
                    'photo': row[2]
                }
                all_dict['partners'].append(partners)

            return jsonify(all_dict)

    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Departments'

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
            # service_json = json.dumps(service_list, indent=4)

            return jsonify(service_list)

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

            show_databases_sql = "SELECT * FROM categories;"
            cursor.execute(show_databases_sql)
            category_data = cursor.fetchall()

            category_list = []
            for row in category_data:
                category_dict = {
                    "category_Id": row[0],
                    "name": row[1],
                    "description": row[2]
                }
                category_list.append(category_dict)

            # Convert the list of dictionaries to JSON
            category_json = json.dumps(category_list, indent=4)

            return jsonify(category_list)

    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Categories'

@app.route('/GetAllInquiries')
def inquiries():

    try:

        return_dict = {}
        cols = ['inquiryId', 'name', 'email', 'serviceInquired', 'meetingDate']

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()

            show_inquiries_sql = "SELECT * FROM Inquiries_Test2;"
            cursor.execute(show_inquiries_sql)
            inquiries_data = cursor.fetchall()

            inquiries_list = []
            for row in inquiries_data:
                inquiries_dict = {
                    "inquiryId" : row[0],
                    "name" : row[1],
                    "email" : row[2],
                    "service_ID" : row[3],
                    "meeting_date" : row[4],
                    "confirmed": row[5]
                }
                inquiries_list.append(inquiries_dict)

            # Convert the list of dictionaries to JSON
            inquiries_json = json.dumps(inquiries_list, indent = 4)

            return jsonify(inquiries_list)
            
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Inquiries'

@app.route('/GetAllOpportunities')
def opportunities():

    try:

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()

            show_inquiries_sql = "SELECT * FROM Opportunities;"
            cursor.execute(show_inquiries_sql)
            inquiries_data = cursor.fetchall()

            opportunities_list = []
            for row in inquiries_data:
                opportunities_dict = {
                    "id" : row[0],
                    "title" : row[1],
                    "location" : row[2],
                    "department" : row[3],
                    "experience_level" : row[4],
                    "description": row[5],
                    "qualifications": row[6],
                    "skills": row[7],
                    "responsibilities": row[8]
                }
                opportunities_list.append(opportunities_dict)

            # Convert the list of dictionaries to JSON
            opportunities_json = json.dumps(opportunities_list, indent = 4)

            return jsonify(opportunities_list)
            
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Opportunities'

@app.route('/GetAllPartners')
def partners():
    # connecting to mariadb
    try:

        return_dict = {}
        cols = ['partnerID', 'name', 'imageData']

        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )	

        if connection.is_connected():
            cursor = connection.cursor()

            show_database_sql = "SELECT * FROM partners;"
            cursor.execute(show_database_sql)
            partners_data = cursor.fetchall()

            partners_list = {}
            for row in partners_data:
                partners_dict = {
                    "partnerID" : row[0],
                    "name" : row[1],
                    "photo" : row[2]
                }

            partners_list.append(partners_dict)

            # Convert the list of dictionaries to JSON
            partners_json = json.dumps(partners_list, indent = 4)

            return jsonify(partners_json)
        
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Partners'


@app.route('/GetAllProjects')
def projects():
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

            show_database_sql = "SELECT * FROM projects;"
            cursor.execute(show_database_sql)
            projects_data = cursor.fetchall()

            projects_list = {}
            for row in projects_data:
                projects_dict = {
                    "id" : row[0],
                    "title" : row[1],
                    "category" : row[2],
                    "description" : row[3],
                    "photo" : row[4],
                    "name" : row[5],
                    "logo_url" : row[6],
                    "year" : row[7]
                }

            projects_list.append(projects_dict)

            # Convert the list of dictionaries to JSON
            projects_json = json.dumps(projects_list, indent = 4)

            return jsonify(projects_json)
        
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Projects'

@app.route('/GetAllTestimonials')
def testimonials():
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

            show_database_sql = "SELECT * FROM testimonials;"
            cursor.execute(show_database_sql)
            testimonials_data = cursor.fetchall()

            testimonials_list = {}
            for row in testimonials_data:
                testimonials_dict = {
                    "id" : row[0],
                    "name" : row[1],
                    "title" : row[2],
                    "testimony" : row[3],
                    "photo" : row[4],
                }

            testimonials_list.append(testimonials_dict)

            # Convert the list of dictionaries to JSON
            testimonials_json = json.dumps(testimonials_list, indent = 4)

            return jsonify(testimonials_json)
        
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    return 'Testimonials'

# Example:
# /getTimeSlots?day=16&month=10&year=2023

@app.route('/getTimeSlots', methods=['GET'])
def get_available_time_slots():
    try:
        day = request.args.get('day', type=int)
        month = request.args.get('month', type=int)
        year = request.args.get('year', type=int)

        # Convert the date parameters to a date string in YYYY-MM-DD format
        date_str = f'{year:04d}-{month:02d}-{day:02d}'

        # Connect to the database
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = conn.cursor()

        # Query the Calendar table for the given date
        cursor.execute("SELECT timeslot_1, timeslot_2, timeslot_3, timeslot_4, timeslot_5 FROM Calendar_Test2 WHERE calendar_date = %s", (date_str,))
        row = cursor.fetchone()

        if row is not None:
            # Get the list of all available time slots
            timeslots = ['10:00', '11:00', '12:00', '13:00', '14:00']
            available_slots = [timeslots[i] for i in range(5) if row[i] is None]

            cursor.close()
            conn.close()

            return jsonify(available_slots)

        cursor.close()
        conn.close()

        return jsonify({'error': 'No data found for the given date'}), 404

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching the schedule data'}), 500


# Example:
# /getTakenDates?month=10&year=2023
@app.route('/getTakenDates', methods=['GET'])
def taken_dates():
    try:
        # Parse query parameters if needed (e.g., month and year)
        month = request.args.get('month', type=int)
        year = request.args.get('year', type=int)

        # Connect to the database
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = conn.cursor()

        # Formulate the SQL query to select days with at least one timeslot booked
        sql_query = f"SELECT DAY(calendar_date) FROM Calendar_Test2 " \
                    f"WHERE YEAR(calendar_date) = {year} " \
                    f"AND MONTH(calendar_date) = {month} " \
                    f"AND (timeslot_1 IS NOT NULL " \
                    f"OR timeslot_2 IS NOT NULL " \
                    f"OR timeslot_3 IS NOT NULL " \
                    f"OR timeslot_4 IS NOT NULL " \
                    f"OR timeslot_5 IS NOT NULL)"

        cursor.execute(sql_query)

        # Fetch the results as a list of days
        result = [row[0] for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching the schedule data'}), 500


# Example:
# /addInquiry?category=1&name=JC%20Diamante&email=jcsd%40gmail.com&timeslot=1&date=2023-10-16
@app.route('/addInquiry', methods=['GET'])
def add_inquiry():

    try:
        CategoryID = request.args.get('category', type=int)
        name = request.args.get('name', type=str)
        email = request.args.get('email', type=str)
        timeslot = request.args.get('timeslot', type=int) # '10:00', '11:00', '12:00', '13:00', '14:00'
        date_arg = request.args.get('date', type=str)

        # CategoryID = 1
        # name = 'JC Diamante'
        # email = 'jdmntec'
        # timeslot = 1
        # date = '2023-10-16'

        # timeslot_1, timeslot_2, timeslot_3, timeslot_4, timeslot_5
        timeslot_list = ['timeslot_1', 'timeslot_2', 'timeslot_3', 'timeslot_4', 'timeslot_5']

        # Connect to the database
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = conn.cursor()

        # make an SQL query that will insert the inquiry to the mysql database

        # Create Inquiry
        sql_query = "INSERT INTO Inquiries_Test2 (name, email, service_ID, meeting_date) VALUES (%s, %s, %s, %s);"
        values = (name, email, CategoryID, date_arg)

        cursor.execute(sql_query, values)

        conn.commit()

        sql_query = "SELECT MAX(inquiryID) FROM Inquiries_Test2;"

        cursor.execute(sql_query)

        rows = cursor.fetchall()

        # Get the last inserted inquiry_id
        max_inquiry_id = int(rows[0][0])

        # Convert date argument (string) to DATE object
        # date_object = datetime.datetime.strptime(date, '%Y-%m-%d').date()

        sql_query = f"UPDATE Calendar_Test2 SET {timeslot_list[timeslot]} = {max_inquiry_id} WHERE calendar_date = '{date_arg}';"

        # UPDATE Calendar_Test2 SET timeslot_2 = NULL WHERE calendar_date = '2023-10-16';

        date_string = date(int(date_arg.split('-')[0]), int(date_arg.split('-')[1]), int(date_arg.split('-')[2])).strftime('%Y-%m-%d')


        cursor.execute(sql_query)

        conn.commit()

        cursor.close()
        conn.close()

        return f'Value Inserted at Inquiry: {max_inquiry_id}'
    
    except Exception as e:
        return f"An error occurred: {e}\n{traceback.format_exc()}"

# comment this out when running in vercel
# app.run() # - uncomment to run in local