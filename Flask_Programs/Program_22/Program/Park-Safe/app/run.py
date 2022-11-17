# %%
from flask import Flask, render_template, request
from geopy.distance import geodesic
import folium
import pickle
import pandas as pd

app = Flask(__name__)


color_grad = ['darkgreen', 'green', 'lightgreen', 'orange', 'pink', 'lightred', 'red', 'darkred']
parking_df = pd.read_csv('../filtered_data/Parking_Spots_Data.csv')
# parking_df = pd.read_csv('../filtered_data/Filtered_Parking_Meter.csv')
prob_color = [0, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7]

with open('../filtered_data/rf.pkl', 'rb') as f:
    model = pickle.load(f)
# %%
def create_and_save_map(coordinates, bound=100):
    folium_map = folium.Map(location=coordinates, zoom_start=14, max_zoom=100)
    folium.map.Marker(coordinates, popup=f'You are here!\n({coordinates[0]},{coordinates[1]})').add_to(folium_map)
    dist = lambda row: geodesic(coordinates, (row.LATITUDE, row.LONGITUDE)).meters
    parking_df['distance'] = parking_df.apply(dist, axis=1)
    filtered_spot_df = parking_df[parking_df['distance']<bound]
    if len(filtered_spot_df)>0:
        filtered_spot_df['theft_prob'] = list(model.predict_proba(filtered_spot_df[['LATITUDE', 'LONGITUDE']])[:, 1])
    for _, spot in filtered_spot_df.iterrows():
        folium.map.Marker((spot.LATITUDE, spot.LONGITUDE), popup=folium.map.Popup(f'<b>meter_ID</b>: {spot.POST_ID}<br/><b>safety_index</b>: {100*(1-spot.theft_prob):.1f}%<br/><b>distance</b>: {int(spot.distance)}m', max_width=150),
         icon=folium.Icon(color=color_grad[prob_color[int(spot.theft_prob*10)]], icon='car', prefix='fa')).add_to(folium_map)
    folium_map.save('templates/map.html')

# %%
@app.route('/', methods=['GET', 'POST'])
def find_parking():
    if request.method == 'GET':
        coordinates = (37.76, -122.44)
        folium_map = folium.Map(location=coordinates, zoom_start=14)
        folium_map.save('templates/map.html')
    else:
        coordinates = (request.form['latitude'], request.form['longitude'])
        create_and_save_map(coordinates, int(request.form['range']))
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
