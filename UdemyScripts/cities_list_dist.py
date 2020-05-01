import time
tmStart = time.time()
parent = iface.mainWindow()
da = QgsDistanceArea()
da.setEllipsoid('WGS84')

layers = QgsProject.instance().mapLayersByName("Countries")
if len(layers)>0:
    countries = layers[0]
    if countries.isValid(): 
        lCntry_names = []
        request = QgsFeatureRequest()
        nmClause = QgsFeatureRequest.OrderByClause("NAME")
        orderby = QgsFeatureRequest.OrderBy([nmClause])
        request.setOrderBy(orderby)
        for cntry in countries.getFeatures(request):
            lCntry_names.append(cntry['NAME'])
        
        sCntry, bOk = QInputDialog.getItem(parent, "City Names", "Select country: ", lCntry_names)
        if bOk:
            for cntry in countries.getFeatures():
                if cntry['NAME'] == sCntry:
                    geomCntry = cntry.geometry()
                    
            layers = QgsProject.instance().mapLayersByName("ne_10m_populated_places")
            if len(layers)>0:
                cities = layers[0]
                if cities.isValid():
                    sStr = "Area of {0} = {1:.3f}\n\n".format(sCntry, da.measureArea(geomCntry)/1000/1000)
                    sStr += "Perimeter of {0} = {1:.3f}\n\n".format(sCntry, da.measurePerimeter(geomCntry)/1000)
                    request = QgsFeatureRequest()
                    popClause = QgsFeatureRequest.OrderByClause("POP_MAX", ascending=False)
                    orderby = QgsFeatureRequest.OrderBy([popClause])
                    request.setOrderBy(orderby)
                    for city in cities.getFeatures(request):
                            if city.geometry().within(geomCntry):
                                dDist = da.measureLine([QgsPointXY(QgsGeometry(city.geometry()).get()), QgsPointXY(-99.5, 19.5)])/1000
                                sStr += "{0:15}{1:10} {2:10.0f}\n".format(city['NAME'], city['POP_MAX'], dDist)
                else:
                    print("'Cities' is not a valid layer")
            else:
                print("Cities was not found")
        else:
            QMessageBox.warning(parent, "Cities", "User canceled")
    else:
        print("'Countries' is not a valid layer")
else:
    print("Countries was not found")

if bOk:            
    tmEnd = time.time()
    sStr = "Run time = {0:.3f} seconds\n\n".format(tmEnd-tmStart) + sStr
    QMessageBox.information(parent, "Cities in {}".format(sCntry), sStr)
   
