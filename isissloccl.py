from tkinter import Y
from colorama import *
from geoloc import *
from issloc import *
from el_dist import *

C = Fore.LIGHTCYAN_EX
Y = Fore.LIGHTYELLOW_EX
M = Fore.LIGHTMAGENTA_EX
W = Fore.LIGHTWHITE_EX
G = Fore.LIGHTGREEN_EX

issloc = IssLocation.GetIssLocation()
geoloc = GeoLocation.GetGeoLocation(input(f"{Y}Input Address:{G} "))

print(f'{Y}Desination: {C}{geoloc}')
print(f'{Y}ISS Position: {C}{issloc}')
print(f'{Y}Elevation Distance: {C}{GeoDistance.GetGeoDistance(geoloc, issloc)}{M}/mi{W}')