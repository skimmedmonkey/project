import requests
import json

# Replace with your API endpoint URL
url = "http://127.0.0.1:8000/compare"

# Prepare the test data with two arrays in the same JSON
data = {
    "data": [
        {"name": "assignment1", "date": "2023-12-31", "source": "array1"},
        {"name": "assignment2", "date": "2024-01-15", "source": "array1"},
        {"name": "assignment3", "date": "2024-02-01", "source": "array1"},
    ],
    "data2": [
        {"name": "assignment1", "date": "2023-12-31", "source": "array2"},
        {"name": "assignment3", "date": "2024-01-16", "source": "array2"},
    ]
}

# Send the POST request with JSON data
response = requests.post(url, json=data)

# Check for successful response
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    print("Discrepancies:")
    for discrepancy in response_data:
        print(f"- Name: {discrepancy['name']}, Date: {discrepancy['date']}")
else:
    print(f"Error: {response.status_code} {response.text}")