"""
Calculations for data and storing them in JSON files 
Nov 2023
"""

# creating US Census API query for the population of each ZCTA within the 2020 Decennial Census
import requests 

host = 'https://api.census.gov/data'
year = '/2020'
dataset_acronym = '/dec/dhc'
g = '?get='
variables = 'P1_001N,NAME' #population variable, can add NAME 
location = '&for=zip%20code%20tabulation%20area%20(or%20part):*&in=state:34' 

usr_key = "&key=52eb42bcce51db27538d66ad91d4ceb476f37c47" #probably should store this in a safer place!!
query_url = f"{host}{year}{dataset_acronym}{g}{variables}{location}{usr_key}"
response = requests.get(query_url)
response_json = response.json()


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