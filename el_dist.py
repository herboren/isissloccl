from geopy import distance

class GeoDistance():
    def GetGeoDistance(destination, source):
        return distance.distance(destination, source).miles