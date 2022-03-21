# /u/inert-

import json, requests, pyfiglet
from geopy.geocoders import Nominatim
from geopy import distance
from marbl import DrawMapMarbleOrtho

# ANSI Color Codes
C = '\033[1;36;40m' # Cyan
Y = '\033[1;33;40m' # Yellow
B = '\033[1;34;40m' # Light Blue
M = '\033[1;35;40m' # Magenta
E = '\033[0;37;40m' # LightGrey
G = '\033[1;32;40m' # Green

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

# Returns ISS reverse for country code
def GetGeoReverseLocation(latlong):
        try:
            geolocator = Nominatim(user_agent="isissloccl.py")
            location = (geolocator.reverse(latlong)).raw['address']['country']
            # Cannot identify working is_land or is_ocean from reliable pysource
            # TryCatch to determine land or sea, so far pretty accurate.
            return location
        except Exception as e:
            return f'{C}Traversing Ocean{E}'

# Simple math, find mileage between two geo-points
def GetGeoDistance(poi, elevatedSource):
        return distance.distance(poi, elevatedSource).miles

physical_address = input(f"{Y}Point of Interest:{G} ")
issloc = GetIssLocation()
geoloc = GetGeoLocation(physical_address)
country = GetGeoReverseLocation(issloc)

print(f'{Y}POI Lat/Long: {G}{geoloc}\n{Y}ISS Lat/Long: {G}{issloc}\n{Y}ISS Country: {M}{country}')
print(f'{Y}Elevation Distance: {G}{round(GetGeoDistance(geoloc, issloc),2)}{M}/mi{E}')

# Draw Map
DrawMapMarbleOrtho.DrawMarble(issloc)
