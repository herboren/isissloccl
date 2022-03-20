from ipyleaflet import Map, basemaps, Marker, basemap_to_tiles
from ipywidgets import Layout

m = Map(
    basemap=basemap_to_tiles(basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08"),
    center=(52.204793, 360.121558),
    zoom=4,
    layout=Layout(width='80%', height='500px')
)

m.add_layer(Marker(location=(52.204793, 360.121558)))

m.save('my_map.html', title='My Map')