# This code creates an API request to a defined endpoint that returns JSON data.

import requests

# Set the base URL for the API
base_url = "https://my.website.com/api"

# Set the API endpoint you want to access
endpoint = "/myCategory/myEndpoint"

# Set the parameters for the API request
params = {
    "param1": "my criteria"
}

# Set the headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <token>"
}

# Make the API request
response = requests.get(base_url + endpoint, params=params, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    # If the request is successful, print the response data
    print(response.json())
else:
    # If the request is not successful, print the error message
    print(f"Request failed: {response.status_code} {response.reason}")