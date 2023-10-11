import mysql.connector

# Define the database configuration
db_config = {
    "host": "3.27.249.230",
    "port": 3306,
    "user": "APIReadOnly",
    "password": "[%BmJz:SoEf72om",
    "database": "ssi",
    "ssl_disabled": True
}

# Connect to the MariaDB server
try:
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Connected to MariaDB Server")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the database connection
    if 'conn' in locals():
        conn.close()
        print("Database connection closed.")
