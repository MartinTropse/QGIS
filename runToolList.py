"""List of common tools and their parameters, for processing.run or "run and load" as well as cmd command"""


###Run tool with processing.run###

#Raster calculator
processing.run("qgis:rastercalculator", {'EXPRESSION':f'\"{sympName}@1\" * \"{ocean}@1\"','LAYERS':[f'E:/GIS/Data/Raster/{ocean}.tif'],'CELLSIZE':250,'EXTENT':None,'CRS':None,'OUTPUT':f'E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyByOcean/{sympName}_{ocean}.tif'})

#Clip raster by vector mask 
processing.run("gdal:cliprasterbymasklayer", param)
param={ 'ALPHA_BAND' : False, 'CROP_TO_CUTLINE' : False, 'DATA_TYPE' : 0, 'EXTRA' : '',\
         'INPUT' : f'E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyByRegion/{regionName}.tif', 'KEEP_RESOLUTION' : False,\
          'MASK' : f'E:/GIS/Data/Raster/ScriptOutdir/Vektor/ProtMaskNollBf/{prct}.shp', 'MULTITHREADING' : False,\
           'NODATA' : None, 'OPTIONS' : 'COMPRESS=PACKBITS', 'OUTPUT' : f'E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyRegionProt/{regionName}__{prct}.tif', \
           'SET_RESOLUTION' : False, 'SOURCE_CRS' : None, 'TARGET_CRS' : None, 'X_RESOLUTION' : None, 'Y_RESOLUTION' : None }

#Buffer 
processing.run("native:buffer", {'INPUT':f'E:/GIS/Data/Raster/ScriptOutdir/Vektor/{name}.shp',\
	'DISTANCE':0,'SEGMENTS':5,'END_CAP_STYLE':0,'JOIN_STYLE':0,'MITER_LIMIT':2,\
	'DISSOLVE':False,'OUTPUT':f'E:/GIS/Data/Raster/ScriptOutdir/Vektor/NollBf/{name}NollBf.shp'})	

#Polygonize (raster to vector)	
processing.run("gdal:polygonize", {'INPUT':f'{rst.source()}','BAND':1,'FIELD':'DN','EIGHT_CONNECTEDNESS':False,'EXTRA':'','OUTPUT':f'E:/GIS/Data/Raster/ScriptOutdir/Vektor/{regionName}.shp'})

#Dissovle
"native:dissolve", {'INPUT':f'E:/GIS/Data/Raster/ScriptOutdir/Vektor/ClipRegionByProt/{lyrName}.shp','FIELD':[],'OUTPUT':'TEMPORARY_OUTPUT'} 
param={ 'ALPHA_BAND' : False, 'CROP_TO_CUTLINE' : False, 'DATA_TYPE' : 0, 'EXTRA' : '','INPUT' : f'E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyByRegion/{regionName}.tif', 'KEEP_RESOLUTION' : False,\'MASK' : f'E:/GIS/Data/Raster/ScriptOutdir/Vektor/ProtMaskNollBf/{prct}.shp', 'MULTITHREADING' : False,\
           'NODATA' : None, 'OPTIONS' : 'COMPRESS=PACKBITS', 'OUTPUT' : f'E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyRegionProt/{regionName}__{prct}.tif', \
           'SET_RESOLUTION' : False, 'SOURCE_CRS' : None, 'TARGET_CRS' : None, 'X_RESOLUTION' : None, 'Y_RESOLUTION' : None }
        processing.run("gdal:cliprasterbymasklayer", param)




####Run GIS tools through cmd###
os.system(gdal_command) # Run command to the CMD, the argument is a string containing cmd command

#Clip raster by vector mask 
gdal_command=f'gdalwarp -of GTiff -cutline E:/GIS/Data/Raster/ScriptOutdir/Vektor/NollBf/{RegionName}.shp -cl {RegionName} \
        -crop_to_cutline -co COMPRESS=PACKBITS E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SweRef99/{SympName}.tif E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyByRegion/{SympName}{RegionName}.tif'

#Convert polygon to raster
gdalCommand=f'gdal_rasterize -l {layer} -burn 1.0 -tr 10.0 10.0 -a_nodata 0.0 -te {xMin} {yMin} {xMax} {yMax} -ot Byte -of GTiff -co COMPRESS=PACKBITS E:/GIS/Data/Vektor/SkyddadNaturData/Edit/{layer}.shp E:/GIS/Data/Vektor/SkyddadNaturData/Edit/{layer}.tif'