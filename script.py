import requests
import smtplib
from googleplaces import GooglePlaces, types, lang
import json
import geopy
def finding_time(lst, num):
     i = 0
     hospitals = []
     while (i < num):
 
         #current address
         current_address = input("Enter your current address\n")

         #hospital adddress
         hospital = input("Enter hospital address\n")

         # base url
         url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
         r=requests.get(url + "origins=" + current_address + "&destinations=" + hospital + "&key=" + "AIzaSyDLnWTNiNuzP5hA-VynTAQuWGAF3hBhHao")
         time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
         lst = lst + [time]
         hospitals += [hospital]
         i += 1

'''
     least_time =  max(lst)
     hospital_index = lst.index(least_time)
     print("The nearest hospital is : \n", hospitals[hospital_index])
     print("Estimated time to reach hospital: ", least_time)

finding_time([], 10)



# Generate an API key by going to this location
# https://cloud.google.com /maps-platform/places/?apis =
# places in the google developers
  
# Use your own API key for making api request calls
API_KEY = 'AIzaSyCox0RNAtah9Rvf3107wvRgP5HR963NT9k'
  
# Initialising the GooglePlaces constructor
google_places = GooglePlaces(API_KEY)
  
# call the function nearby search with
# the parameters as longitude, latitude,
# radius and type of place which needs to be searched of 
# type can be HOSPITAL, CAFE, BAR, CASINO, etc
query_result = google_places.nearby_search(
        # lat_lng ={'lat': 46.1667, 'lng': -1.15},
        lat_lng ={'lat': 28.4089, 'lng': 77.3178},
        radius = 5000,
        # types =[types.TYPE_HOSPITAL] or
        # [types.TYPE_CAFE] or [type.TYPE_BAR]
        # or [type.TYPE_CASINO])
        types =[types.TYPE_HOSPITAL])
  
# If any attributions related 
# with search results print them
if query_result.has_attributions:
    print (query_result.html_attributions)
  
  
# Iterate over the search results
for place in query_result.places:
    # print(type(place))
    # place.get_details()
    print (place.name)
    print("Latitude", place.geo_location['lat'])
    print("Longitude", place.geo_location['lng'])
    print()



'''
