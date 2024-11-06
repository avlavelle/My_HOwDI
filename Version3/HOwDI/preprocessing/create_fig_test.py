import matplotlib.pyplot as plt
import geopandas as gpd
def create_arcs(create_fig=True, shpfile='US_COUNTY_SHPFILE/US_county_cont.shp'):
    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
    if shpfile is None:
        # logger.warning()
        print(
            "An arcs figure is being generated but no underlying shapefile exists!"
        )
    else:
        # TODO make generic
        us_county = gpd.read_file(shpfile)
        ##us = us_county.dissolve().to_crs(epsg=epsg)
        us = us_county.to_crs(epsg=epsg)
        us.plot(ax=ax, color="white", edgecolor="black")
        ##tx_county = us_county[us_county["STATE_NAME"] == "Texas"]
        ##tx = tx_county.dissolve().to_crs(epsg=epsg)
        ##tx.plot(ax=ax, color="white", edgecolor="black")
    plt.show()
    fig.savefig("fig.png")
    return fig

if __name__ == "__main__":
    create_arcs()