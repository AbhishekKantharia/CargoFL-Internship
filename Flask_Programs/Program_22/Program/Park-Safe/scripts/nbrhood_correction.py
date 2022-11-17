# Use incident co-ordinates and geojson polygons to figure out the neighborhood
# %% 
import math
from shapely.geometry import Polygon, Point
import pandas as pd
import json

# %%
incident_df = pd.read_csv('../filtered_data/Filtered_Incident_Report2.csv')
with open('../filtered_data/sf_neighborhoods.geojson', 'r') as f:
    geo_data = json.load(f)

# %%

nbr_to_poly = dict()
for nbr in geo_data['features']:
    nbr_to_poly[nbr['properties']['name']] = Polygon(nbr['geometry']['coordinates'][0][0])
# %%
nbr_adjusted = list()
for lon, lat in zip(incident_df['Longitude'], incident_df['Latitude']):
    correct_nbr = None
    if not math.isnan(lon):
        p = Point(lon, lat)
        for nbr, polygon in nbr_to_poly.items():
            if polygon.contains(p):
                correct_nbr = nbr
                break
    nbr_adjusted.append(correct_nbr)
# %%
incident_df.drop('Unnamed: 0', axis=1, inplace=True)
incident_df['neighborhood_adjusted'] = nbr_adjusted
incident_df.to_csv('../filtered_data/Filtered_Incident_Report2.csv')
# %%
