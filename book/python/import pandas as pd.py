import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString

# Input and output files
input_csv = "survey01.csv"
output_gpkg = "output_lines.gpkg"
layer_name = "troncons"  # name of the layer inside the GeoPackage

# Read CSV
df = pd.read_csv(input_csv, encoding="latin-1")

column_name = "capturedetroncon"
if column_name not in df.columns:
    raise ValueError(f"Column '{column_name}' not found.")

lines = []

for value in df[column_name]:
    if pd.isna(value):
        lines.append(None)
        continue

    points = []
    point_strings = str(value).split(";")

    for pt in point_strings:
        parts = pt.strip().split()

        # Format: lat lon altitude precision
        if len(parts) >= 2:
            lat = float(parts[0])
            lon = float(parts[1])
            points.append([lon, lat])  # shapely uses (x, y) = (lon, lat)

    # Create line only if at least two points
    if len(points) >= 2:
        lines.append(LineString(points))
    else:
        lines.append(None)
print (points)
'''# Create GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=lines, crs="EPSG:4326")

# Save to GeoPackage
gdf.to_file(output_gpkg, layer=layer_name, driver="GPKG")

print(f"GeoPackage created: {output_gpkg}")
'''

