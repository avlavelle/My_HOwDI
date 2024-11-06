import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim  # necessary installation, unnecessary import
import csv
from shapely.geometry import Point

def get_county(latitude,longitude):
    geolocator = Nominatim(user_agent="HOwDI")
    location = geolocator.reverse((latitude,longitude), exactly_one=True)
    if location:
        address = location.raw
        county = address["address"]["county"]
        return county
    else:
        return None
    
def get_state(latitude,longitude):
    geolocator = Nominatim(user_agent="HOwDI")
    location = geolocator.reverse((latitude,longitude), exactly_one=True)
    if location:
        address = location.raw
        state = address["address"]["state"]
        return state
    else:
        return None
    
def main():
    county = get_county(29.18161,-95.4993375)
    print(county)
    state = get_state(29.18161,-95.4993375)
    print(state)


if __name__ == "__main__":
    main()