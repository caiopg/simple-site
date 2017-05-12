from flask import Flask, render_template
import candlechart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/plot')
def plot():
    comps = candlechart.plot()
    cdn = candlechart.fetch_cdn()

    return render_template("plot.html", cdn_css = cdn["cdn_css"], cdn_js = cdn["cdn_js"],

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
