from geopy.geocoders import Nominatim
from math import sin, cos, sqrt, atan2


city1 = input("Enter the name of the first city ~> ")
city2 = input("Enter the name of the second city ~> ")

print("Processing...")
geolocator = Nominatim(user_agent="pydist")

try:
    location1 = geolocator.geocode(city1)
    location2 = geolocator.geocode(city2)
    lat1 = location1.latitude
    print("Latitude of ", city1, " is ", lat1)
    lon1 = location1.longitude
    print("Longitude of ", city1, " is ", lon1)

    lat2 = location2.latitude
    print("Latitude of ", city2, " is ", lat1)

    lon2 = location2.longitude
    print("Longitude of ", city2, " is ", lon2)

    dlon = lat2 - lat1  # difference between the two latitudes
    dlat = lon2 - lon1  # difference between the two longitudes

    # radius of the earth in km
    R = 6373.0

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    print("The distance between the two cities is ~> ", distance, "km")
except:  # catching all errors coz am too lazy
    print("An error occured. Probably too many requests. :)")
