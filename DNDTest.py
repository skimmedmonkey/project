import requests
import json

# Replace with your API endpoint URL
url = "http://127.0.0.1:8000/api/compare/"

# Prepare the test data with two arrays in the same JSON
data = {
    "array1": [
        {"name": "assignment1", "date": "2023-12-31"},
        {"name": "assignment2", "date": "2024-01-15"},
        {"name": "assignment3", "date": "2024-02-01"}
    ],
    "array2": [
        {"name": "assignment1", "date": "2023-12-31"},
        {"name": "assignment3", "date": "2024-01-16"}
    ]
}

# Send the POST request with JSON data
response = requests.post(url, json=data)

# Check for successful response
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    print("API Response:")
    print(json.dumps(result, indent=2))
else:
    print(f"API Request Failed with Status Code: {response.status_code}")
    print(response.text)