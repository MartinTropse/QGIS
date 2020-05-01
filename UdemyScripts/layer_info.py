parent = iface.mainWindow()
mc = iface.mapCanvas()
lyrs = mc.layers()
lLyrNames = []
for lyr in lyrs:
    if isinstance(lyr, QgsVectorLayer):
        lLyrNames.append(lyr.sourceName())
        
sLyr, bOk = QInputDialog.getItem(parent, "Visible Layers", "Select a layer: ", lLyrNames)
if bOk:
    lyr = QgsProject.instance().mapLayersByName(sLyr)[0]
    if lyr.isValid():
        sStr = QgsWkbTypes.displayString(lyr.wkbType())
        sStr += "\n{}".format(lyr.crs().description())
        request = QgsFeatureRequest()
        request.setLimit(10)
        cnt = 0
        for ftr in lyr.getFeatures(request):
            cnt += 1
            sStr += "\nFeature {}".format(cnt)
            geom = QgsGeometry.constGet(ftr.geometry())
            sStr += "\n    Parts: {}".format(geom.partCount())
            cntR = 0
            cntV = 0
            for part in ftr.geometry().constParts():
                cntR += part.ringCount()
                cntV += part.vertexCount()
                print(type(part))
            sStr += "\n    Rings: {}".format(cntR)
            sStr += "\n    Vertices: {}".format(cntV)
         
        QMessageBox.about(parent, "About {}".format(sLyr), sStr)
    else:
        QMessageBox.warning(parent, "Warning", "Layer '{}' is not valid".format(sLyr))
else:
    QMessageBox.warning(parent, "Warning", "User canceled")
    
