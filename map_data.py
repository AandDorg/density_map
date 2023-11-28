"""
Calculations for data and storing them in JSON files 
Nov 2023
"""

# creating US Census API query for the population of each ZCTA within the 2020 Decennial Census
import requests 
import json

host = 'https://api.census.gov/data'
year = '/2020'
dataset_acronym = '/dec/dhc'
g = '?get='
variables = 'P1_001N,NAME' #population variable, can add NAME 
location = '&for=zip%20code%20tabulation%20area:*'

#'&for=zip%20code%20tabulation%20area%20(or%20part):*&in=state:*' 

usr_key = "&key=52eb42bcce51db27538d66ad91d4ceb476f37c47" #probably should store this in a safer place!!
query_url = f"{host}{year}{dataset_acronym}{g}{variables}{location}{usr_key}"
response = requests.get(query_url)
response_json = response.json()

#making json data structure: 
all_ZCTA_json = {}

for j in range(1, (len(response_json))):
    new_entry = {}
    for i in range(len(response_json[0])-1):
        each_parameter = response_json[0][i]
        new_entry[each_parameter] = response_json[j][i]
    all_ZCTA_json[response_json[j][2]] = new_entry

json_object = json.dumps(all_ZCTA_json) 
with open("ZCTA_population_data.json", "w") as outfile:
    outfile.write(json_object)
   