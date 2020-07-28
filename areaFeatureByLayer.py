#Script that iterates over vector layers (should add if statement to chk if vector layer) and gives the area of each feature
#Need to add the name and output locations

import pandas as pd

mc=iface.mapCanvas() #iface works automatically from console, otherwise requires import: from qgis.utils import iface
layers=mc.layers() #Adds all layers that are currently checked in the TOC

nameList = []
areaList = []

for layer in layers:
    lyrName=layer.sourceName()
    nameList.append(lyrName)
    processing.runAndLoadResults("native:dissolve", {'INPUT':f'E:/GIS/Data/Raster/ScriptOutdir/Vektor/ClipRegionByProt/{lyrName}.shp','FIELD':[],'OUTPUT':'TEMPORARY_OUTPUT'})
    dissLayer=QgsProject.instance().mapLayersByName('Dissolved')[0]
    ftrs = dissLayer.getFeatures()
    if len(list(dissLayer.getFeatures())) == 0:
        areaList.append(0)
        QgsProject.instance().removeMapLayer(dissLayer)
    else:
        val = 0
        for ftr in ftrs:
            if val == 0:
                areaList.append(ftr.geometry().area()) #Probably good to check that this adds up, that CRS is projected etc. 
                val += 1
        QgsProject.instance().removeMapLayer(dissLayer)

df=pd.DataFrame()

df['Name'] = nameList
df['Area'] = areaList 

df.to_csv("", encoding='latin-1', index=False) #Add name and location of the output file 
