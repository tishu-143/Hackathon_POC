from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("template.html")

if __name__ == "__main__":
    app.run()


