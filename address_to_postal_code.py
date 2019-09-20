import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='d')

def get_postal_code_from_address(address: str, client: googlemaps.Client):
    return client.places(address)['results'][0]['formatted_address'][-6:]

def get_info_from_coordinate(lat: float, lng: float, client: googlemaps.Client):
    return client.reverse_geocode((lat, lng))

def get_postal_code_from_coordinate(lat: float, lng: float, client: googlemaps.Client):
    temp = get_info_from_coordinate(lat, lng, client)
    for i in temp[0]['address_components']:
        if i['types'][0] == 'postal_code':
            return i['long_name']

addr = 'Temasek Hall'
coor = (1.291545370107278, 103.7700234701073)

# print(get_postal_code_from_address(addr, gmaps))
print(get_postal_code_from_coordinate(coor[0], coor[1], gmaps))
