import time
tmStart = time.time()

layers = QgsProject.instance().mapLayersByName("ne_10m_populated_places")
if len(layers)>0:
    countries = layers[0]
    if countries.isValid():
        print(countries.crs())
        sStr = ""
        request = QgsFeatureRequest()
        popClause = QgsFeatureRequest.OrderByClause("POP_MAX", ascending=False)
        orderby = QgsFeatureRequest.OrderBy([popClause])
        request.setOrderBy(orderby)
        request.setLimit(10)
        for ftr in countries.getFeatures(request):
                sStr += "{0:15}{1:10}, {2:20}\n".format(ftr['NAME'], ftr['POP_MAX'], ftr.geometry().asWkt(5))
        print(sStr)
    else:
        print("'Countries' is not a valid layer")
else:
    print("Countries was not found")
    
tmEnd = time.time()
print("Run time = {0:.3f} seconds".format(tmEnd-tmStart))