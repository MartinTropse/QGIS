mc = iface.mapCanvas()
lyr = mc.currentLayer()
crs = lyr.crs()
print(crs.postgisSrid())
print(crs.toWkt())
print(crs.toProj4())
print(crs.description())
crs=QgsCoordinateReferenceSystem(26913)
print(crs.postgisSrid())
print(crs.toWkt())
print(crs.toProj4())
print(crs.description())
crs = QgsCoordinateReferenceSystem.fromProj4("+proj=longlat +datum=WGS84 +no_defs")
print(crs.description())