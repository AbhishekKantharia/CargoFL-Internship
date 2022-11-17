#%%
import pandas as pd

data_df = pd.read_csv('../data/Police_Department_Incident_Reports__2018_to_Present.csv')
parking_meter_df = pd.read_csv('../data/Parking_Meters.csv')
# %%
filtered_data_df = data_df.filter(['Incident Datetime', 'Incident Description', 'Analysis Neighborhood', 'Intersection', 'Latitude', 'Longitude'], axis=1)
filtered_data_df = filtered_data_df.loc[[desc.startswith('Vehicle, Stolen') for desc in filtered_data_df['Incident Description']], :]
filtered_data_df.to_csv('../filtered_data/Filtered_Incident_Report.csv')
# %%
filtered_parking_meter_df = parking_meter_df.filter(['POST_ID', 'ACTIVE_METER_FLAG', 'LATITUDE', 'LONGITUDE'], axis=1)
filtered_parking_meter_df = filtered_parking_meter_df[filtered_parking_meter_df['ACTIVE_METER_FLAG']=='M']
filtered_parking_meter_df.drop(['ACTIVE_METER_FLAG'], axis=1, inplace=True)
filtered_parking_meter_df.to_csv('../filtered_data/Filtered_Parking_Meter.csv')
# %%

filtered_data_df2 = data_df.filter(['Incident Datetime', 'Incident Subcategory', 'Analysis Neighborhood', 'Intersection', 'Latitude', 'Longitude'], axis=1)
filtered_data_df2['Incident Subcategory']=filtered_data_df2['Incident Subcategory'].fillna('No cathegory')
filtered_data_df2 = filtered_data_df2[filtered_data_df2['Incident Subcategory'].str.contains("Vehicle")]
filtered_data_df2.to_csv('../filtered_data/Filtered_Incident_Report2.csv')
