from flask import Flask, render_template
import folium
import tishant

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("section.html")

@app.route("/template.html")
def template():
    return render_template("template.html")

@app.route("/tishant.html")
def tishant_Page():
    return tishant.folium_map()

@app.route("/Nimish.html")
def nimish():
    return render_template("Nimish.html")

@app.route("/section.html")
def section():
    return render_template("section.html")

if __name__ == "__main__":
    app.run()


