import re

root = QgsProject().instance().layerTreeRoot()

pattern=re.compile(r'\w+Poly.+')

for layer in root.children():
    lyrHit=re.search(pattern, layer.name())
    if lyrHit:
    	processing.run("gdal:cliprasterbymasklayer", {'INPUT':'E:/GIS/Data/Raster/Jobbdator_Lager/HavRegioner/BLEKINGE/BLEKINGEHav.tif', 'MASK':layer.name(),'SOURCE_CRS':None,'TARGET_CRS':None,'NODATA':None,'ALPHA_BAND':False,'CROP_TO_CUTLINE':True,'KEEP_RESOLUTION':False,'SET_RESOLUTION':False,'X_RESOLUTION':None,'Y_RESOLUTION':None,'MULTITHREADING':False,'OPTIONS':'','DATA_TYPE':1,'EXTRA':'','OUTPUT':f'E:/GIS/Data/SandBox/{layer.name()}.tif'})
print("Im done mam!")