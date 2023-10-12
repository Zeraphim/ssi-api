# How to use
# http://127.0.0.1:5000/api/hello

from flask import Flask, request, jsonify
import mysql.connector
import json
import base64
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

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


@app.route('/')
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


@app.route('/getAllProjects')
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
			return jsonify(project_dict)

	except mysql.connector.Error as error:
		print("Error: {}".format(error))

	finally:
		if 'connection' in locals() and connection.is_connected():
			cursor.close()
			connection.close()
			print("MySQL connection is closed.")

	return 'Projects'


@app.route('/getAllOpportunity')
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
			# project_json = json.dumps(opportunity_list, indent=4)

			return jsonify(opportunity_dict)

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

@app.route('/GetAllInquiry')
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

			show_inquiries_sql = "SELECT * FROM SERVICES;"
			cursor.execute(show_inquiries_sql)
			inquiries_data = cursor.fetchall()

			inquiries_list = []
			for row in inquiries_data:
				inquiries_dict = {
					"inquiryId" : row[0],
					"name" : row[1],
					"email" : row[2],
					"serviceInquired" : row[3],
					"meetingDate" : row[4]
				}
				inquiries_list.append(inquiries_dict)

			# Convert the list of dictionaries to JSON
			inquiries_json = json.dumps(inquiries_list, indent = 4)

			return inquiries_json
			
	except mysql.connector.Error as error:
		print("Error: {}".format(error))
	
	finally:
		if 'connection' in locals() and connection.is_connected():
			cursor.close()
			connection.close()
			print("MySQL connection is closed.")

	return 'Inquiries'

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

			show_database_sql = "SELECT * FROM CATEGORY;"
			cursor.execute(show_database_sql)
			partners_data = cursor.fetchall()

			partners_list = {}
			for row in partners_data:
				partners_dict = {
					"partnerID" : row[0],
					"name" : row[1],
					"imageData" : row[2]
				}

			partners_list.append(partners_dict)

			# Convert the list of dictionaries to JSON
			partners_json = json.dumps(partners_list, indent = 4)

			return partners_json
		
	except mysql.connector.Error as error:
		print("Error: {}".format(error))
	
	finally:
		if 'connection' in locals() and connection.is_connected():
			cursor.close()
			connection.close()
			print("MySQL connection is closed.")

	return 'Partners'

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

# comment this out when running in vercel
app.run() # - uncomment to run in local