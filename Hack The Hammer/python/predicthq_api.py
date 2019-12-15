import json
import requests

#global data dictionary
data = []

#adds a bunch of events to the data dictionary
def update_data(limit=0, offset=0):
    response = requests.get("http://api.predicthq.com/v1/events", 
        headers={
            "Authorization": "Bearer BEh_s0y9Wf8kilmTJJn1QAwhqEgcVWOIdf_0G4hN",
            "Accept": "application/json"
        },
        params={
            "country":"CA",
            "label":"technology,science,design",
            "offset":offset,
            "limit":limit
        }
    )
    new_data = response.json()
    data.append(new_data["results"])

#updates the json file
def add_to_json():
    try:
        with open("data.json", "w") as data_file:
            json.dump(data, data_file)
    except FileNotFoundError:
            "data file is missing"
    except TypeError:
        "Error, cannot encode type to json"

#calls from the api a lot of times, as limited accounts can only pull 20 entries at a time
for i in [i for i in range(0, 50)]:
    update_data(1, i)

add_to_json()