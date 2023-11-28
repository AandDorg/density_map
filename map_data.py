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

#Take this list of lists.... create each entry where {P1_001N : ....etc.}

all_ZCTA_json = {}

for j in range(1, (len(response_json))):
    new_entry = {}
    for i in range(len(response_json[0])-1):
        each_parameter = response_json[0][i]
        new_entry[each_parameter] = response_json[j][i]
    #new_entry_json = json.dumps(new_entry)
    #print(type(new_entry_json))
    all_ZCTA_json[response_json[j][2]] = new_entry

#print(all_ZCTA_json)

json_object = json.dumps(all_ZCTA_json) 
with open("ZCTA_population_data.json", "w") as outfile:
    outfile.write(json_object)
   



"""

import csv, json

county_population_list = []

with open('co-est2022-alldata.csv', mode = 'r') as file: 
    us_population_data = list(csv.reader(file))

    for row in us_population_data[1:]: 
        county_name = str(row[6])
        state_name = str(row[5])
        population_2022 = int(row[10])

        county_data = {
            'county': county_name,
            'state' : state_name,
            'population' : population_2022
        }

        county_population_list.append(county_data)

with open('simplemaps_uscounties_basicv1.73/uscounties.csv', mode = 'r') as file: 
    county_lat_long_data = list(csv.reader(file))

    for row in county_lat_long_data[1:]: 
        county_name = str(row[2])
        state_name = str(row[5])
        county_lat = float(row[6])
        county_long = float(row[7])
        
        for each_county in county_population_list: 
            if (each_county['county'] == county_name and each_county['state'] == state_name):
                each_county['latitude'] = county_lat
                each_county['longitude'] = county_long

with open('data_to_use.json', 'w') as f:     
    json.dump(county_population_list, f)

"""