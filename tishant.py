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
providers = list(data['Providers'])
members = list(data['Members'])



def folium_map():
    m = folium.Map(location = [0, 0], zoom_start = 2)
    for con, lt, ln, prd, pic, prds, mem in zip(country, LAT, LON, provider, picture, providers, members):
        m.add_child(folium.Marker(location = [lt, ln], icon = folium.Icon('hospital') ,tooltip="Click on the icon for information", popup = "<br>State : "+con+" <br> Provider Center : "+prd+" <br> Total Providers : "+str(prds)+" <br> Total Covid Patients : "+str(mem)+"<br><img src = "+pic+" height = 142, width = 290>"))
    return render_template("template.html")+m._repr_html_()+render_template("footer.html")