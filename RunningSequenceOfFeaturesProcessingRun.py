layer = QgsProject.instance().mapLayersByName('GridMask')[0]

for nr in range(1, len(list(layer.getFeatures()))):
    layer.selectByExpression(f"\"id\" = {nr}")
    new_layer = layer.materialize(QgsFeatureRequest().setFilterFids(layer.selectedFeatureIds()))
    QgsProject.instance().addMapLayer(new_layer)
    processing.run("gdal:cliprasterbymasklayer", {'INPUT':'E:/GIS/Data/Raster/AllSkyddadeOmrd/Blekinge/BLEKINGEHav.tif','MASK':new_layer,'SOURCE_CRS':None,'TARGET_CRS':None,'NODATA':None,\
    	'ALPHA_BAND':False,'CROP_TO_CUTLINE':True,'KEEP_RESOLUTION':False,'SET_RESOLUTION':False,'X_RESOLUTION':None,'Y_RESOLUTION':None,'MULTITHREADING':False,'OPTIONS':'','DATA_TYPE':0,\
    	'EXTRA':'','OUTPUT':f'E:/GIS/Data/Raster/AllSkyddadeOmrd/Blekinge/{nr}CutRaster.tif'})
