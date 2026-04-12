from ipyleaflet import Map, GeoJSON
from shiny import reactive
from shiny.express import input, render, ui
from shinywidgets import render_widget
import json
import random
import requests
import os

ui.page_opts(title="New York State", fillable=True)
{"class": "bslib-page-dashboard"}

with ui.sidebar():
    ui.input_dark_mode(mode="dark")

if not os.path.exists('us-states.json'):
    url = 'https://github.com/jupyter-widgets/ipyleaflet/raw/master/examples/us-states.json'
    r = requests.get(url)
    with open('us-states.json', 'w') as f:
        f.write(r.content.decode("utf-8"))

with open('us-states.json', 'r') as f:
    data = json.load(f)

def random_color(feature):          # ← body was unindented before
    return {
        'color': 'black',
        'fillColor': random.choice(['red', 'yellow', 'green', 'orange']),
    }

with ui.card(full_screen=True):
    @render_widget
    def map():
        m = Map(center=(50.6252978589571, 0.34580993652344), zoom=3)

        geo_json = GeoJSON(
            data=data,
            style={
                'opacity': 1, 'dashArray': '9', 'fillOpacity': 0.1, 'weight': 1
            },
            hover_style={
                'color': 'white', 'dashArray': '0', 'fillOpacity': 0.5
            },
            style_callback=random_color
        )
        m.add(geo_json)

        return m                    # ← was unindented before