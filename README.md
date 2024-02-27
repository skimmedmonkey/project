# DNDApp Project
Welcome to my project! My webapp utilizes Python and Django to help users who are interested in Dungeons and Dragon get information about monsters, items and create characters.

## Description
Aside from the Dungeons and Dragons aspect, where the user can get information about Monsters, Items and Build Characters, it also provides a simple API microservice that 
can receive JSON data containing two arrays (array1 and array2) of assignment names and dates. Then it will compare the two arrays for matching assignment names, and check 
to see if the second array of dates is different to the first. If it is, it will output JSON with the assignment name and date from the differing second array.

## Communication Contract

### API Endpoint
This project provides a RESTful API for comparing names and dates. The API endpoint for the comparison is `/api/compare/`. Users should make POST requests to this endpoint 
with JSON data containing two arrays of names and dates. If you are running this locally, the endpoint will be 'http://127.0.0.1:8000/api/compare/'.

### Example Call (in Python)
import requests
import json

"""Replace with your API endpoint URL"""
url = "http://127.0.0.1:8000/api/compare/"

"""Send the POST request with JSON data"""
response = requests.post(url, json=data)

"""Check for successful response"""
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    print("API Response:")
    print(json.dumps(result, indent=2))
else:
    print(f"API Request Failed with Status Code: {response.status_code}")
    print(response.text)

### Example Call (from terminal when run locally)
curl -X POST -H "Content-Type: application/json" --data @test.json http://127.0.0.1:8000/api/compare/

### Input JSON Format
The expected JSON format for input data is shown below:
{
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

### UML sequence diagram
![DNDAppAPI](https://github.com/skimmedmonkey/project/assets/129809154/ce89fe74-cb6a-40fd-b3ca-107a96a559a4)
