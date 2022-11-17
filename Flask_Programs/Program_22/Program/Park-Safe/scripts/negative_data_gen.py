# %%
import pandas as pd
import numpy as np

incident_df = pd.read_csv('../filtered_data/Filtered_Incident_Report.csv')
negative_df_path = '../filtered_data/Negative_Incident.csv'
incident_df.shape
# %%
from datetime import datetime

incident_df['Incident Datetime'] = list(map(lambda x: datetime.strptime(x, '%Y/%m/%d %I:%M:%S %p'), incident_df['Incident Datetime']))
filter_dt = lambda dt: (dt.year==2019)
incident_2019_df = incident_df.loc[incident_df['Incident Datetime'].apply(filter_dt), :][['Incident Datetime', 'Latitude', 'Longitude']].dropna()
# %%
hour = incident_2019_df['Incident Datetime'].apply(lambda dt: dt.hour).tolist()
dow = incident_2019_df['Incident Datetime'].apply(lambda dt: dt.weekday()).tolist()
month = incident_2019_df['Incident Datetime'].apply(lambda dt: dt.month).tolist()
latitude = incident_2019_df['Latitude'].tolist()
longitude = incident_2019_df['Longitude'].tolist()
label = [1]*incident_2019_df.shape[0]
# %%
neg_count = 6*incident_2019_df.shape[0]
for _ in range(neg_count):
    hour.append(np.random.randint(24))
    dow.append(np.random.randint(7))
    month.append(np.random.randint(1, 13))
    latitude.append(np.random.uniform(37.708, 37.830))
    longitude.append(np.random.uniform(-122.511, -122.364))    
    label.append(0)
# %%
pd.DataFrame({'hour': hour, 
              'dow': dow,
              'month': month,
              'latitude': latitude,
              'longitude': longitude,
              'label': label}).to_csv(negative_df_path)
# %%
