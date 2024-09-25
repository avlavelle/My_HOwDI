import json
import pandas as pd

def get_unique_counties(geojson_file):
    with open(geojson_file, 'r') as f:
        data = json.load(f)

    unique_counties = set()
    for hub in data["features"]:
        county = hub["properties"]["County"]
        if county is not None:
            unique_counties.add(county)
    
    return list(unique_counties)

if __name__ == "__main__":
    counties = get_unique_counties("hubs.geojson")
    print(counties)
    county_dataframe = pd.DataFrame(counties, columns=["County"])
    county_dataframe.to_csv('new_unique_counties.csv', index=False)