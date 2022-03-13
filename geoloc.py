from geopy.geocoders import Nominatim

class GeoLocation():

    def GetGeoLocation(loc):
        try:
            geolocator = Nominatim(user_agent="isissloccl.py")
            location = geolocator.geocode(loc)            
            geoloc = (location.latitude, location.longitude)
            return geoloc
        except Exception as e:
            print(e)