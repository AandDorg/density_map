"""
Calculations for data and storing them in JSON files 


Data fields by city? 
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