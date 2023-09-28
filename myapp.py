import requests
import json

# Define the API endpoint URLs for GetAllPartners, GetAllCareers, GetAllProjects, and AddInquiry
api_url_partners = "https://personal-jsxgxps8.outsystemscloud.com/testapi_service/rest/v1/partners/{PartnersId}"
api_url_careers = "https://personal-jsxgxps8.outsystemscloud.com/testapi_service/rest/v1/careers/{CareersId}"
api_url_projects = "https://personal-jsxgxps8.outsystemscloud.com/testapi_service/rest/v1/projects/{ProjectsId}"
api_url_inquiry = "https://personal-jsxgxps8.outsystemscloud.com/testapi_service/rest/v1/inquiries"

# Function to fetch data from the API and handle JSON response
def fetch_data(api_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    }
    
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except json.decoder.JSONDecodeError:
            print("Error: Invalid JSON response")
            return None
    else:
        print(f"Error: {response.status_code}")
        return None

# Function to print data in JSON format
def print_data_as_json(data, task_name):
    print(f"{task_name} Data:")
    print(json.dumps(data, indent=4))

# Fetch data from GetAllPartners
partners_data = fetch_data(api_url_partners)

if partners_data:
    # Print data for Partners
    print_data_as_json(partners_data, "Partners")

# Fetch data from GetAllCareers
careers_data = fetch_data(api_url_careers)

if careers_data:
    # Print data for Careers
    print_data_as_json(careers_data, "Careers")

# Fetch data from GetAllProjects
projects_data = fetch_data(api_url_projects)

if projects_data:
    # Print data for Projects
    print_data_as_json(projects_data, "Projects")

# Example: Sending data to AddInquiry
inquiry_data = {
    "Message": "This is an inquiry message.",
    "Name": "John Doe",
    "Email": "john.doe@example.com"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}

response = requests.post(api_url_inquiry, json=inquiry_data, headers=headers)

if response.status_code == 200:
    inquiry_response_data = response.json()
    # Print data for AddInquiry
    print_data_as_json(inquiry_response_data, "AddInquiry Response")
    print("\nInquiry added successfully.")
else:
    print(f"Error adding inquiry: {response.status_code}")
