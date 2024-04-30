import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim  # necessary installation, unnecessary import
import csv
from shapely.geometry import Point

def get_county(latitude,longitude):
    geolocator = Nominatim(user_agent="HOwDI")
    location = geolocator.reverse((latitude,longitude), exactly_one=True)
    if location:
        address = location.address
        for word in address.split(","):
            if ("County") in word:
                county = word.lstrip()
        return county
    else:
        return None
    
def main():
    county = get_county(33.71742,-116.171)
    print(county)


if __name__ == "__main__":
    main()