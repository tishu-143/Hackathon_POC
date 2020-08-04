import folium
from flask import Flask, render_template
import pandas as pd
import base64

data = pd.read_csv("Providers.csv")

country = list(data['Country'])
provider = list(data['Provider Center'])
LAT = list(data['Latitude'])
LON = list(data['Longitude'])
picture = list(data['Picture'])



def folium_map():
    m = folium.Map(location = [33, -117], zoom_start = 10)
    for con, lt, ln, prd in zip(country, LAT, LON, provider):
        popup = folium.Popup("<br> Country : "+con+" <br> Provider Center : "+prd+" <br>", max_width = 2500)
        marker = folium.Marker([lt, ln], popup=popup).add_to(m)
        m.add_child(marker)
    return render_template("template.html")+m._repr_html_()+render_template("footer.html")