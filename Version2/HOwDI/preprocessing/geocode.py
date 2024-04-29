import pandas as pd
import geopandas as gpd
##from geopy.geocoders import Nominatim  # necessary installation, unnecessary import
import csv
from shapely.geometry import Point
##import geojson

"""
def camel_case_split(str):
    # adapted from https://www.geeksforgeeks.org/python-split-camelcase-string-to-individual-strings/
    words = [[str[0]]]

    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    words = ["".join(word) for word in words]
    words[0] = words[0].capitalize()
    return " ".join(words)
"""

"""
def geocode_hubs(file="hubs.csv"):
    Generates a GeoJSON file from geocoded locations of hub (detailed hubs.csv)

    hubs = pd.read_csv(file)["hub"].tolist()
    hubs_cc = [camel_case_split(hub) + ", Texas" for hub in hubs]

    geohubs = gpd.tools.geocode(
        hubs_cc, provider="nominatim", user_agent="HOwDI"
    ).set_index(pd.Series(hubs, name="hub"))

    geohubs["County"] = [
        word.lstrip()
        for words in geohubs["address"].str.split(",")
        for word in words
        if ("County") in word
    ]

    return geohubs
"""
##def geocode_hubs(file="hubs.csv",geojson_file_path="hubs.geojson"):
def geocode_hubs(file="hub_dir/hubs.csv"):
    ## features = []
    hubs = pd.read_csv(file)
    geometry = [Point(xy) for xy in zip(hubs['longitude'],hubs['latitude'])]

    geohubs = gpd.GeoDataFrame(hubs, geometry=geometry)
    geohubs = geohubs.drop(columns=['latitude','longitude'])
    ##with open(file, 'r') as csvfile:
     ##   reader = csv.DictReader(csvfile)

    """    for row in reader:
            hub = row['hub']
            latitude = row['latitude']
            longitude = row['longitude']

            if latitude and longitude:
                try:
                    latitude = float(latitude)
                    longitude = float(longitude)

                    feature = geojson.Feature(
                        geometry=geojson.Point((longitude, latitude)),
                        properties={'hub': hub}
                    )

                    features.append(feature)
                except ValueError as e:
                    print(f"Couldn't process row {row}. {e}")
    geohubs = geojson.FeatureCollection(features)
    with open(geojson_file_path, 'w') as geojsonfile:
        geojson.dump(geohubs, geojsonfile, indent=1)
"""
    return geohubs

def main():
    geohubs = geocode_hubs()
    geohubs.to_file("hubs.geojson", driver="GeoJSON")


if __name__ == "__main__":
    main()
