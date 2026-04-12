
# ---------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------
import ipyleaflet as L
from faicons import icon_svg
from geopy.distance import geodesic, great_circle
from shared import BASEMAPS, CITIES
from shiny import reactive
from shiny.express import input, render, ui
from shinywidgets import render_widget

def update_marker(map: L.Map, loc: tuple, on_move: object, name: str):
    remove_layer(map, name)
    m = L.Marker(location=loc, draggable=True, name=name)
    m.on_move(on_move)
    map.add_layer(m)


def update_line(map: L.Map, loc1: tuple, loc2: tuple):
    remove_layer(map, "line")
    map.add_layer(
        L.Polyline(locations=[loc1, loc2], color="blue", weight=2, name="line")
    )


def update_basemap(map: L.Map, basemap: str):
    for layer in map.layers:
        if isinstance(layer, L.TileLayer):
            map.remove_layer(layer)
    map.add_layer(L.basemap_to_tiles(BASEMAPS[basemap]))


def remove_layer(map: L.Map, name: str):
    for layer in map.layers:
        if layer.name == name:
            map.remove_layer(layer)


def on_move1(**kwargs):
    return on_move("loc1", **kwargs)


def on_move2(**kwargs):
    return on_move("loc2", **kwargs)


# When the markers are moved, update the selectize inputs to include the new
# location (which results in the locations() reactive value getting updated,
# which invalidates any downstream reactivity that depends on it)
def on_move(id, **kwargs):
    loc = kwargs["location"]
    loc_str = f"{loc[0]}, {loc[1]}"
    choices = city_names + [loc_str]
    ui.update_selectize(id, selected=loc_str, choices=choices)
