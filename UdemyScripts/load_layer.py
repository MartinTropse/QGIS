"""   Load a Shapefile    """
parent = iface.mainWindow()

fns, fnOK = QFileDialog.getOpenFileNames(parent,"Shapefiles to open", QgsProject.instance().homePath(),"Shape Files (*.shp);;GeoJSON Files (*.geojson)")
if fnOK:
    QMessageBox.information(parent, "Success", "Opening {}...".format(fns))
    for fn in fns:
        iface.addVectorLayer(fn, "New Layer", "ogr")
else:
    QMessageBox.warning(parent, "Warning", "No file selected")
