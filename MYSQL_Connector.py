import mysql.connector
# import  pymysql
import os
import time

import random
import string
from datetime import datetime, timedelta

import json



# this is a comment
# this is a test
# test comment Gabriel Deveraturda
# inserted data to services

# Connection parameters
# host = 'localhost'
# user = 'ssiadmin'
# password = 'root321'
# database = 'mysql'

import mariadb
import sys

# Admin (Read/Write)
# host = "13.229.7.124"
# user = "OSAdmin"
# password = "uK4FQkoYqNDHfzC"
# database = "ssi"

# Admin (Instance)
# host = "3.27.249.230"
# user = "OSAdmin"
# password = "uK4FQkoYqNDHfzC"
# database = "ssi"

# Remote Admin
host = "3.27.249.230"
user = "remoteAdmin"
password = "adminTest1"
database = "ssi"

# Api Read Only
# host = "ec2-13-211-161-99.ap-southeast-2.compute.amazonaws.com"
# user = "APIReadOnly"
# password = "[%BmJz:SoEf72om"
# database = "ssi"


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
                f"\n> {'='*9} S S I  D B {'='*9} <\n\n1: Show All Databases\n2: Show Tables \n3. Run Command\n4. Pic Upload\n5. Insert Data\n6: Exit\n")
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

                # Partners Insert
                q = """INSERT INTO partners (name, photo) VALUES (%s, %s);"""
                convertPic = convertToBinary(
                    r"/Users/zeraphim/Desktop/SSI-Images/logos/AWS1.png")
                values = ("AWS", convertPic)
 
                cursor.execute(q, values)

                # Projects Insert
                # q = """INSERT INTO Projects (name, description, photo, category) VALUES (%s, %s, %s, %s);"""
                # convertPic = convertToBinary(
                #     r"/Users/zeraphim/Desktop/SSI-Images/webp_images/c2-travelapp.webp")
                # values = ("Travel Companion App", "A travel companion mobile application for a client.", convertPic, 2)

                # cursor.execute(q, values)

            elif response == "5":

                # Inquiries Insert Statements
                # names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
                # services = [1, 2, 3, 4, 5]
                # emails = ['{}@example.com'.format(name.lower()) for name in names]
                # dates = [datetime.now() + timedelta(days=i) for i in range(3)]
                # confirmed = [True, False]

                # names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
                # services = [1, 2, 3, 4, 5]
                # emails = ['{}@example.com'.format(name.lower()) for name in names]
                # dates = [datetime.now() + timedelta(days=i) for i in range(3)]
                # confirmed = [True, False]

                # for i in range(3):
                #     name = random.choice(names)
                #     email = random.choice(emails)
                #     service = random.choice(services)
                #     date = random.choice(dates).strftime('%Y-%m-%d')
                #     is_confirmed = random.choice(confirmed)

                #     q = """INSERT INTO Inquiries (name, email, serviceInquired, meetingDate, isConfirmed)
                #         VALUES (%s, %s, %s, %s, %s);"""
                #     values = (name, email, service, date, is_confirmed)
                
                #cursor.execute(q, values)

                # Opportunities

                data = [
                    {
                        "title": "Software Developer",
                        "location": "New York",
                        "department": "Engineering",
                        "experience_level": "Entry Level",
                        "description": "We are looking for a software developer to join our team.",
                        "qualifications": ["BS degree in Computer Science", "MS degree in Software Engineering"],
                        "skills": ["Java", "Python", "SQL"],
                        "responsibilities": "Develop and maintain software applications."
                    },
                    {
                        "title": "Marketing Manager",
                        "location": "Los Angeles",
                        "department": "Marketing",
                        "experience_level": "Mid Level",
                        "description": "We are hiring a Marketing Manager to lead our marketing campaigns.",
                        "qualifications": ["Bachelor's degree in Marketing", "MBA in Marketing"],
                        "skills": ["Digital marketing", "SEO", "SEM"],
                        "responsibilities": "Plan and execute marketing strategies."
                    },
                    {
                        "title": "Sales Representative",
                        "location": "Chicago",
                        "department": "Sales",
                        "experience_level": "Entry Level",
                        "description": "Join our sales team and help us drive revenue growth.",
                        "qualifications": ["High School diploma", "Sales training certification"],
                        "skills": ["Sales", "Negotiation", "Communication"],
                        "responsibilities": "Identify and approach potential clients."
                    }
                ]

                # Define the SQL query to insert data, using JSON format for qualifications and skills
                insert_query = "INSERT INTO Opportunities (title, location, department, experience_level, description, qualifications, skills, responsibilities) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

                # Execute the query with the JSON data for qualifications and skills
                for row in data:
                    qualifications_json = json.dumps(row['qualifications'])
                    skills_json = json.dumps(row['skills'])
                    values = (row['title'], row['location'], row['department'], row['experience_level'], row['description'], qualifications_json, skills_json, row['responsibilities'])
                    cursor.execute(insert_query, values)


            elif response == "6":
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
