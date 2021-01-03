import requests
import json
url = "https://covid-19-india2.p.rapidapi.com/details.php"

headers = {
    'x-rapidapi-key': "d9103e1a05msh1ed909b134cb933p127c8ejsn516998dec800",
    'x-rapidapi-host': "covid-19-india2.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
r_dict = json.loads(response.text)
states = list(r_dict.keys())[1:-1]  # list of all state name
print(states)
for i in states:
    state_data = r_dict.get(i)      # Use you list to give state by index
    print(f"State No.: {state_data['slno']}")
    print(f"State Name: {state_data['state']}")
    print(f"Confirm Cases: {state_data['confirm']}")
    print(f"Cured Cases: {state_data['cured']}")
    print(f"Total Deaths: {state_data['death']}")
    print(f"Total Cases: {state_data['total']}", end="\n\n")