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
    m = folium.Map(location = [0, 0], zoom_start = 2)
    for con, lt, ln, prd, pic in zip(country, LAT, LON, provider, picture):
        m.add_child(folium.Marker(location = [lt, ln], popup = "<br>State : "+con+" <br> Provider Center : "+prd+" <img src = "+pic+" height = 142, width = 290>"))
    return render_template("template.html")+m._repr_html_()+render_template("footer.html")