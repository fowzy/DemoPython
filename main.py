import json
from sre_constants import IN
from numpy import append
from rich import print
import random
import pandas as pd

def makeLines(cities):
    feature = {
    "type": "Feature",
    "properties": {
        "marker-color": randColor(),
    },
        "geometry": {
            "type": "LineString",
            "coordinates": []
        }
    }
    for city in cities:
        if city['geometry']['coordinates']:
            x = city['geometry']['coordinates'][0]
            y = city['geometry']['coordinates'][1]
            feature['geometry']['coordinates'].append([x,y])
            # feature['geometry']['coordinates'][0] = x
            # feature['geometry']['coordinates'][1] = y
    return feature
# create the header of geo json aka feature collection
def makeFeatureCollection(cities):
    FeatureCollection = {}
    FeatureCollection["type"] = "FeatureCollection"
    FeatureCollection["features"] = cities
    return FeatureCollection

# random color generator
def randColor():
    def r(): return random.randint(0, 255)
    return ('#%02X%02X%02X' % (r(), r(), r()))

"""
                         /$$                                           /$$             /$$
                        | $$                                          |__/            | $$
 /$$$$$$/$$$$   /$$$$$$ | $$   /$$  /$$$$$$         /$$$$$$   /$$$$$$  /$$ /$$$$$$$  /$$$$$$
| $$_  $$_  $$ |____  $$| $$  /$$/ /$$__  $$       /$$__  $$ /$$__  $$| $$| $$__  $$|_  $$_/
| $$ \ $$ \ $$  /$$$$$$$| $$$$$$/ | $$$$$$$$      | $$  \ $$| $$  \ $$| $$| $$  \ $$  | $$
| $$ | $$ | $$ /$$__  $$| $$_  $$ | $$_____/      | $$  | $$| $$  | $$| $$| $$  | $$  | $$ /$$
| $$ | $$ | $$|  $$$$$$$| $$ \  $$|  $$$$$$$      | $$$$$$$/|  $$$$$$/| $$| $$  | $$  |  $$$$/
|__/ |__/ |__/ \_______/|__/  \__/ \_______/      | $$____/  \______/ |__/|__/  |__/   \___/
                                                  | $$
                                                  | $$
                                                  |__/

"""
# This function needs to pass the city dict and rank in order to return feature geo json point
def makePoint(city, rank):
    feature = {
        "type": "Feature",
        "properties": {
            "marker-color": randColor(),
            "marker-symbol": rank,
            "population": '',
            "city" :'',
            "state": ''
        },
    "geometry": {
      "type": "Point",
      "coordinates": [0,0]
    }
    }
    # assign the coordinates to the feature dict   
    for i in city['properties']:
        if i == 'geometry':
            cord1 = float(city['properties']['geometry']['coordinates'][0])
            cord2 = float(city['properties']['geometry']['coordinates'][1])
            feature['geometry']['coordinates'][0] = cord1
            feature['geometry']['coordinates'][1] = cord2
        if i == 'properties':
            feature['properties']['population'] = city['properties']['properties']['population']
            feature['properties']['city'] = city['properties']['properties']['city']
            feature['properties']['state'] = city['properties']['properties']['state']

    return feature


"""
 /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$
| $$__  $$| $$_____/ /$$__  $$| $$__  $$|_  $$_/| $$$ | $$ /$$__  $$
| $$  \ $$| $$      | $$  \ $$| $$  \ $$  | $$  | $$$$| $$| $$  \__/
| $$$$$$$/| $$$$$   | $$$$$$$$| $$  | $$  | $$  | $$ $$ $$| $$ /$$$$
| $$__  $$| $$__/   | $$__  $$| $$  | $$  | $$  | $$  $$$$| $$|_  $$
| $$  \ $$| $$      | $$  | $$| $$  | $$  | $$  | $$\  $$$| $$  \ $$
| $$  | $$| $$$$$$$$| $$  | $$| $$$$$$$/ /$$$$$$| $$ \  $$|  $$$$$$/
|__/  |__/|________/|__/  |__/|_______/ |______/|__/  \__/ \______/

    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
   |__  $$ /$$__  $$ /$$__  $$| $$$ | $$
      | $$| $$  \__/| $$  \ $$| $$$$| $$
      | $$|  $$$$$$ | $$  | $$| $$ $$ $$
 /$$  | $$ \____  $$| $$  | $$| $$  $$$$
| $$  | $$ /$$  \ $$| $$  | $$| $$\  $$$
|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$
 \______/  \______/  \______/ |__/  \__/
"""
# Change path as appropriate
with open("almost_geojson.json") as f:
    data = json.load(f)

"""
  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$  /$$$$$$$$
 /$$__  $$|__  $$__//$$__  $$| $$__  $$| $$_____/
| $$  \__/   | $$  | $$  \ $$| $$  \ $$| $$
|  $$$$$$    | $$  | $$  | $$| $$$$$$$/| $$$$$
 \____  $$   | $$  | $$  | $$| $$__  $$| $$__/
 /$$  \ $$   | $$  | $$  | $$| $$  \ $$| $$
|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$| $$$$$$$$
 \______/    |__/   \______/ |__/  |__/|________/

 /$$$$$$ /$$   /$$ /$$$$$$$$ /$$$$$$
|_  $$_/| $$$ | $$|__  $$__//$$__  $$
  | $$  | $$$$| $$   | $$  | $$  \ $$
  | $$  | $$ $$ $$   | $$  | $$  | $$
  | $$  | $$  $$$$   | $$  | $$  | $$
  | $$  | $$\  $$$   | $$  | $$  | $$
 /$$$$$$| $$ \  $$   | $$  |  $$$$$$/
|______/|__/  \__/   |__/   \______/

 /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$$
| $$__  $$|_  $$_/ /$$__  $$|__  $$__/
| $$  \ $$  | $$  | $$  \__/   | $$
| $$  | $$  | $$  | $$         | $$
| $$  | $$  | $$  | $$         | $$
| $$  | $$  | $$  | $$    $$   | $$
| $$$$$$$/ /$$$$$$|  $$$$$$/   | $$
|_______/ |______/ \______/    |__/

"""
# make states list to store only state
states = {}
for item in data:
    state = item["properties"]["properties"]["state"]
    city = item["properties"]["properties"]["city"]
    population = item["properties"]["properties"]["population"]
    #coordinates = item["properties"]["properties"]["coordinates"]
    # filter Hawaii and Alaska
    if (state not in states) and (state != "Alaska" and state != "Hawaii"):
        states[state] = []
    # get the city with population if the state in the states list
    if(state in states):
        # states[state].append({'city': city,'population': population})
        states[state].append(item)

"""
  /$$$$$$              /$$
 /$$__  $$            | $$
| $$  \__/  /$$$$$$  /$$$$$$
| $$ /$$$$ /$$__  $$|_  $$_/
| $$|_  $$| $$$$$$$$  | $$
| $$  \ $$| $$_____/  | $$ /$$
|  $$$$$$/|  $$$$$$$  |  $$$$/
 \______/  \_______/   \___/

 /$$                                                           /$$
| $$                                                          | $$
| $$        /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$
| $$       |____  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$_____/|_  $$_/
| $$        /$$$$$$$| $$  \__/| $$  \ $$| $$$$$$$$|  $$$$$$   | $$
| $$       /$$__  $$| $$      | $$  | $$| $$_____/ \____  $$  | $$ /$$
| $$$$$$$$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$ /$$$$$$$/  |  $$$$/
|________/ \_______/|__/       \____  $$ \_______/|_______/    \___/
                               /$$  \ $$
                              |  $$$$$$/
                               \______/
  /$$$$$$  /$$   /$$
 /$$__  $$|__/  | $$
| $$  \__/ /$$ /$$$$$$   /$$   /$$
| $$      | $$|_  $$_/  | $$  | $$
| $$      | $$  | $$    | $$  | $$
| $$    $$| $$  | $$ /$$| $$  | $$
|  $$$$$$/| $$  |  $$$$/|  $$$$$$$
 \______/ |__/   \___/   \____  $$
                         /$$  | $$
                        |  $$$$$$/
                         \______/
"""
largest_cities = []
for state in states:
    # create a pop list that has all the population of the cities in each state
    populations = []
    # going through the cities
    for city in states[state]:
        population = city["properties"]["properties"]["population"]
        # append the population
        populations.append(population)
    # get the laregest poulation city in the state
    largestPopulation = max(populations)
    # get the index of that city so I could identify what city it was
    largestCity = populations.index(largestPopulation)
    # find the name of the city by using index
    largest_cities.append(states[state][largestCity])

"""
 /$$      /$$  /$$$$$$  /$$   /$$ /$$$$$$$$
| $$$    /$$$ /$$__  $$| $$  /$$/| $$_____/
| $$$$  /$$$$| $$  \ $$| $$ /$$/ | $$
| $$ $$/$$ $$| $$$$$$$$| $$$$$/  | $$$$$
| $$  $$$| $$| $$__  $$| $$  $$  | $$__/
| $$\  $ | $$| $$  | $$| $$\  $$ | $$
| $$ \/  | $$| $$  | $$| $$ \  $$| $$$$$$$$
|__/     |__/|__/  |__/|__/  \__/|________/



 /$$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$ /$$$$$$
| $$__  $$ /$$__  $$|_  $$_/| $$$ | $$|__  $$__//$$__  $$
| $$  \ $$| $$  \ $$  | $$  | $$$$| $$   | $$  | $$  \__/
| $$$$$$$/| $$  | $$  | $$  | $$ $$ $$   | $$  |  $$$$$$
| $$____/ | $$  | $$  | $$  | $$  $$$$   | $$   \____  $$
| $$      | $$  | $$  | $$  | $$\  $$$   | $$   /$$  \ $$
| $$      |  $$$$$$/ /$$$$$$| $$ \  $$   | $$  |  $$$$$$/
|__/       \______/ |______/|__/  \__/   |__/   \______/



 /$$$$$$ /$$   /$$
|_  $$_/| $$$ | $$
  | $$  | $$$$| $$
  | $$  | $$ $$ $$
  | $$  | $$  $$$$
  | $$  | $$\  $$$
 /$$$$$$| $$ \  $$
|______/|__/  \__/



  /$$$$$$  /$$$$$$$$  /$$$$$$           /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
 /$$__  $$| $$_____/ /$$__  $$         |__  $$ /$$__  $$ /$$__  $$| $$$ | $$
| $$  \__/| $$      | $$  \ $$            | $$| $$  \__/| $$  \ $$| $$$$| $$
| $$ /$$$$| $$$$$   | $$  | $$            | $$|  $$$$$$ | $$  | $$| $$ $$ $$
| $$|_  $$| $$__/   | $$  | $$       /$$  | $$ \____  $$| $$  | $$| $$  $$$$
| $$  \ $$| $$      | $$  | $$      | $$  | $$ /$$  \ $$| $$  | $$| $$\  $$$
|  $$$$$$/| $$$$$$$$|  $$$$$$/      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$
 \______/ |________/ \______/        \______/  \______/  \______/ |__/  \__/



"""

# using sorted method to sort cities by population using lambda
sortedCities = sorted(largest_cities, key=lambda x: x['properties']['properties']['population'])
# make points for geo json and passing the rank by population
points = []
for i in range(len(sortedCities)):
    points.append(makePoint(sortedCities[i], i))

# create lines to connect states or the largest cities together
points.append(makeLines(points))

# Change path as appropriate
with open("output.geojson", "w") as f:
    json.dump(makeFeatureCollection(points), f, indent=4)
