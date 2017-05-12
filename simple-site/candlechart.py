from pandas_datareader import data
from datetime import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

def status_value(op, cl):
    if op > cl:
        return "Decrease"
    elif cl > op:
        return "Increase"
    else:
        return "Equal"

def plot(source="GOOG"):
    start = datetime(2015, 11, 1)
    end = datetime(2016, 3, 10)

    df = data.DataReader(source, data_source="yahoo", start=start, end=end)

    p = figure(x_axis_type="datetime", width=1000, height=300, responsive=True)
    p.title.text = "Candlestick Chart"
    p.grid.grid_line_alpha = 0.3

    df["Status"] = [status_value(op, cl) for op, cl in zip(df.Open, df.Close)]
    df["MiddleOC"] = (df.Open+df.Close)/2
    df["HeightOC"] = abs(df.Open-df.Close)

    hours_12 = 12 * 60 * 60 * 1000

    p.segment(df.index, df.High, df.index, df.Low, color="black")

    p.rect(df.index[df.Status=="Increase"], df.MiddleOC[df.Status=="Increase"],
           hours_12, df.HeightOC[df.Status=="Increase"],fill_color="#ccffff", line_color="black")

    p.rect(df.index[df.Status=="Decrease"], df.MiddleOC[df.Status=="Decrease"],
           hours_12, df.HeightOC[df.Status=="Decrease"],fill_color="#ff3333", line_color="black")

    comp_dict = {}
    comp_dict["script"], comp_dict["div"] = components(p)
    return comp_dict

def fetch_cdn():
    infos = {}
    infos["cdn_js"] = CDN.js_files[0]
    infos["cdn_css"] = CDN.css_files[0]

    return infos
