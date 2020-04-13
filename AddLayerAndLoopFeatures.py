fn = "C:/MartinTropse/GIS/Projects/HaV_Skyddadeomraden/HaV.gpkg|layername=LanOchHavPoly"
layer = iface.addVectorLayer(fn, '', ogr)

for field in layer.fields():
    print(field)