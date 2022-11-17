# %%
import folium
import json
import pandas as pd
from copy import deepcopy
from ipywidgets import interact
from datetime import datetime
# %%
sf_neighborhood_geo = '../filtered_data/sf_neighborhoods.geojson'
sf_loc = (37.76, -122.44)

with open(sf_neighborhood_geo, 'r') as f:
    geo_data = json.load(f)

incident_df = pd.read_csv('../filtered_data/Filtered_Incident_Report2.csv')
incident_df = incident_df[['Incident Datetime', 'neighborhood_adjusted']]
incident_df['Incident Datetime'] = list(map(lambda x: datetime.strptime(x, '%Y/%m/%d %I:%M:%S %p'), incident_df['Incident Datetime']))
# incident_df.replace(['Bayview Hunters Point', 'Financial District/South Beach', 'Sunset/Parkside', 'Castro/Upper Market', 'Lone Mountain/USF', 'Oceanview/Merced/Ingleside', 'Twin Peaks', 'Presidio', 'Lincoln Park'],
#                     ['Bayview', 'Financial District', 'Parkside', 'Castro', 'Lone Mountain', 'Oceanview', 'Upper Market', 'Presidio Heights', 'Lincoln Park / Ft. Miley'], inplace=True)
# %%


def create_map(data):
    gdata = deepcopy(geo_data)
    data_idx = data.set_index('Neighborhood')
    for nbr in gdata['features']:
        nbr['properties']['theft_count'] = 0
        if nbr['properties']['name'] in data_idx.index.values:
            nbr['properties']['theft_count'] = str(data_idx.loc[nbr['properties']['name']]['Theft Count'])

    sf_choropleth = folium.features.Choropleth(
        geo_data=gdata,
        data=data,
        columns=['Neighborhood', 'Theft Count'],
        key_on='properties.name',
        fill_color='PuRd',
        nan_fill_color='White',
        highlight=True
    )

    folium.features.GeoJsonTooltip(['name','theft_count'], ['Neighborhood', 'Theft Count']).add_to(sf_choropleth.geojson)
    sf_map = folium.Map(location=sf_loc, zoom_start=11)
    sf_choropleth.add_to(sf_map)

    return sf_map

# %%


month_options = ['All', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
dow_options = ['All', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


@interact(year=['All', 2018, 2019, 2020],
          month=month_options,
          dow=dow_options,
          hour=['All']+list(range(24)))
def plot_neigborhood_crime(year, month, dow, hour):
    month = month_options.index(month) if month!='All' else month
    dow = dow_options.index(dow)-1 if dow!='All' else dow
    filter_dt = lambda dt: (year=='All' or dt.year==year) and (month=='All' or dt.month==month) and (dow=='All' or dt.weekday()==dow) and (hour=='All' or dt.hour==hour)
    filter_df = (incident_df.loc[[filter_dt(dt) for dt in incident_df['Incident Datetime']], :]
                 .groupby(['neighborhood_adjusted'], as_index=False)
                 .count()
                 .rename(columns={'Incident Datetime': 'Theft Count',
                                  'neighborhood_adjusted': 'Neighborhood'})
                 )

    return create_map(filter_df)
# %%
import matplotlib.pyplot as plt
crime_count_by_nbr = incident_df['neighborhood_adjusted'].value_counts()
plt.xlabel('#vehicle crime')
crime_count_by_nbr[:10].plot(kind='barh')
