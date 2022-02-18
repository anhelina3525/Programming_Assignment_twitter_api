"""
This module displays locations of people
in your twitter 'following' section.
"""
from geopy.geocoders import Nominatim, ArcGIS
from folium import FeatureGroup, Marker, LayerControl, Map, Icon
import json
from twitter2 import get_dict_twitter
def display_locations(nickname):
    """
    This function shows the locations
    of people in your friend list using
    geopy and folium module.
    """
    dictionary = get_dict_twitter(nickname)
    my_map = Map()
    geolocator = ArcGIS(user_agent='app')
    new_dict = {}
    users = dictionary['users']
    for user in users:
        name = user['screen_name']
        loc = user['location']
        if loc:
            location = geolocator.geocode(loc)
            new_dict[name] = (loc, location.latitude, location.longitude)
            Marker(location=(location.latitude, location.longitude), popup=name+'\n'+loc, icon=Icon(color='pink')).add_to(my_map)
    my_map.save('templates/friends_locations.html')
