import json, requests, pyfiglet
from geopy.geocoders import Nominatim
from geopy import distance
from global_land_mask

# ANSI Color Codes
C = '\033[1;36;40m'
Y = '\033[1;33;40m'
M = '\033[1;35;40m'
LG = '\033[0;37;40m'
G = '\033[1;32;40m'

# Banner
label = pyfiglet.figlet_format('ISS-Tracker', font='standard')
print(f'\033[1;35;40m{label}')

 # This will get the current location of
 # the ISS Space Station in low earth orbit.
def GetIssLocation():
        # Request URL
        isslocurl = 'http://api.open-notify.org/iss-now.json'
        response = requests.get(isslocurl)
        issjson = json.loads(response.text)

        # Get values of keys
        longlat = [float(issjson['iss_position']['latitude']),float(issjson['iss_position']['longitude'])]       
        return longlat

# Point of Interest geolocator, returns long/lat
def GetGeoLocation(loc):
        try:
            geolocator = Nominatim(user_agent="isissloccl.py")
            location = geolocator.geocode(loc)            
            geoloc = [float(location.latitude),float(location.longitude)]
            return geoloc
        except Exception as e:
            print(e)

# Point of Interest geolocator, returns long/lat
def GetGeoReverseLocation(latlong):
        try:
            geolocator = Nominatim(user_agent="isissloccl.py")
            location = geolocator.reverse(latlong)
            #country = location.raw['country']
            print(location)
            return location
        except Exception as e:
            print(e)

# Simple math, find mileage between two geo-points
def GetGeoDistance(poi, elevatedSource):
        return distance.distance(poi, elevatedSource).miles

physical_address = input(f"{Y}Point of Interest:{G} ")
issloc = GetIssLocation()
geoloc = GetGeoLocation(physical_address)
co = GetGeoReverseLocation(issloc)

print(f'{Y}POI Lat/Long: {C}{geoloc}')
print(f'{Y}ISS Lat/Long: {C}{issloc}')
print(f'{Y}ISS Country: {C}{co}')
print(f'{Y}Elevation Distance: {C}{GetGeoDistance(geoloc, issloc)}{M}/mi{LG}')