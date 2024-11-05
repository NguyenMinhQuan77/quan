import googlemaps
from datetime import datetime

gmaps = googlemaps.client(key='qwejsakhdqw')
distance = gmaps.geocode('DHGTVT')
reverse_geocode = gmaps.reverse_geocode((long , lat))
now = datetime.now()
direction = gmaps.directions("hanoi", "noibai", mode="transit", departure_time=)


