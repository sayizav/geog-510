import math 
import h3
import geopandas as gpd
from shapely.geometry import Polygon

print(math.sqrt(16))
'''
def gps_to_h3_geopackage(latitude, longitude, resolution, output_path):

    # resolution
    if resolution < 0 or resolution > 15:
        raise ValueError("H3 resolution must be between 0 and 15")

    # Get index from GPS point
    h3_index = h3.latlng_to_cell(latitude, longitude, resolution)
    # Get hexagon (lat, lon pairs)
    boundary = h3.cell_to_boundary(h3_index)

    # Convert to shapely polygon (lon, lat order for GIS)
    polygon = Polygon([(lng, lat) for lat, lng in boundary])

    # Create GeoDataFrame
    gdf = gpd.GeoDataFrame(
        {"h3_index": [h3_index], "latitude": [latitude], "longitude": [longitude], "resolution": [resolution]}, geometry=[polygon], crs="EPSG:4326"
    )

    # Export to GeoPackage
    gdf.to_file(output_path, driver="GPKG")

    print(f"H3 index: {h3_index}")
    print(f"GeoPackage saved to: {output_path}")



    
# Example coordinate (Bujumbura area)
lat = -3.36420
lon = 29.39906
res = 7
output_file = "h3_hexagon_res7.gpkg"
gps_to_h3_geopackage(lat, lon, res, output_file)
'''