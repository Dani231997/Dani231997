import os
import requests

# Define the API endpoint URL
url = "https://scraptik.p.rapidapi.com/search-users"

# Define the query parameters
querystring = {
    "keyword": "claraycandela",
    "count": "20",
    "cursor": "0"
}

# Read the API key from the environment variable
api_key = os.getenv("RAPIDAPI_KEY")

# Check if the API key is set; raise an error if not
if not api_key:
    raise ValueError("No RAPIDAPI_KEY environment variable set")

# Define the headers, including the API key
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "scraptik.p.rapidapi.com"
}

# Make the GET request to the API endpoint
response = requests.get(url, headers=headers, params=querystring)

# Print the JSON response from the API
print(response.json())