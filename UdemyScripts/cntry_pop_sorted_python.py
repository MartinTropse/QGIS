import time

tmStart = time.time()

layers = QgsProject.instance().mapLayersByName("Countries")
if len(layers)>0:
    countries = layers[0]
    if countries.isValid():
        request = QgsFeatureRequest()
        request.setFilterExpression("\"POP_EST\" > 100000")
        lCountries = []
        for ftr in countries.getFeatures(request):
            lCountries.append(ftr['NAME'])
        
        lCountries.sort()
        
        sResult = ""
        for cntry in lCountries:
            request = QgsFeatureRequest()
            request.setFilterExpression("\"NAME\" = '{}'".format(cntry))
            for ftr in countries.getFeatures(request):
                if ftr['POP_EST']>100000000:
                    pop_cat = "large"
                elif ftr['POP_EST']<10000000:
                    pop_cat = 'small'
                else:
                    pop_cat = 'moderate'
                
                sResult += "{} has a {} population\n".format(ftr['NAME'], pop_cat)

    else:
        print("'Countries' is not a valid layer")
else:
    print("Countries was not found")
    
tmEnd = time.time()
print(sResult)
print("Run time = {0:.3f} seconds".format(tmEnd-tmStart))    