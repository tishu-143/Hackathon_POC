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

@app.route("/orgs-map")
def tishant_Page():
    return tishant.folium_map()

@app.route("/vaccination.html")
def vaccination():
    return render_template("vaccination.html")

@app.route("/CovidInfo.html")
def covid_info():
    return render_template("CovidInfo.html")

@app.route('/Covid-19-stats.html')
def covid_jyotish():
    return render_template("Covid-19-stats.html")



@app.route("/pandemic.html")
def pandemic():
    return render_template("pandemic.html")

@app.route("/section.html")
def section():
    return render_template("section.html")

if __name__ == "__main__":
    app.run()


