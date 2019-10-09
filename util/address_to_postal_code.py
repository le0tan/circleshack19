import googlemaps
from datetime import datetime
import geopy.distance

gmaps = googlemaps.Client(key='this key is expired anyway')

def get_postal_code_from_address(address: str, client: googlemaps.Client):
    return get_detail_from_address(address)['results'][0]['formatted_address'][-6:]

def get_info_from_coordinate(lat: float, lng: float, client: googlemaps.Client):
    return client.reverse_geocode((lat, lng))

def get_postal_code_from_coordinate(lat: float, lng: float, client: googlemaps.Client):
    temp = get_info_from_coordinate(lat, lng, client)
    for i in temp[0]['address_components']:
        if i['types'][0] == 'postal_code':
            return i['long_name']

def get_detail_from_address(address: str, client: googlemaps.Client):
    return client.places(address)

# Sample return value: {'lat': 1.2927579, 'lng': 103.7713629}
def get_coordinate_from_detail(detail):
    return detail['results'][0]['geometry']['location']

# Sample return value: 0.37328561721780706 km
def distance_between_coordinates(c1, c2):
    coords_1 = (c1['lat'], c1['lng'])
    coords_2 = (c2['lat'], c2['lng'])
    return geopy.distance.geodesic(coords_1, coords_2)

addr = 'Temasek Hall'
coor = get_coordinate_from_detail(get_detail_from_address(addr, gmaps))
addr2 = 'School of Computing, NUS'
coor2 = get_coordinate_from_detail(get_detail_from_address(addr2, gmaps))

# print(get_postal_code_from_address(addr, gmaps))
# print(get_postal_code_from_coordinate(coor[0], coor[1], gmaps))
print(distance_between_coordinates(coor, coor2))
