import folium
from flask import Flask, render_template

def folium_map():
    m = folium.Map(location = [42, -71], zoom_start = 10)
    return render_template("template.html")+m._repr_html_()+render_template("footer.html")