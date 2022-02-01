import folium
import pandas
df=pandas.read_csv("IndiaVolcanoes.txt")
lat=list(df["LAT"])
lon=list(df["LON"])
elev=list(df["ELEV"])

def color_check(elevation):
    if elevation > 2000:
        return "red"
    elif elevation > 1000 and elevation < 1999:
        return "orange"
    else :
        return "green"
map=folium.Map(location=[19.5512,74.9281],tiles="Stamen Terrain")
map.add_child(folium.Marker(location=[19.5512,74.9281],popup="Hi I am Here",icon=folium.Icon(color='green')))

fgv=folium.FeatureGroup(name="Volcanoes")
for lt,ln,elv in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=10,popup=str(elv)+'m',color='grey',fill_color=color_check(elv),fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <=x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")