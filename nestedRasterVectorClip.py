#Nested loop to run a list of vectors over all selected raster layers
#and clips out new rasters layers. 

mc=iface.mapCanvas()
layers=mc.layers() #needs to be raster, should add if to check

protList = ['OBO_NollBuff','Natura2000_NollBuff','NR_NollBuffer','NP_NollBuff']

for prct in protList:
    for lyr in layers:
        print("Here goes a layer!")
        regionName=lyr.name()
        param={ 'ALPHA_BAND' : False, 'CROP_TO_CUTLINE' : False, 'DATA_TYPE' : 0, 'EXTRA' : '',\
         'INPUT' : f'E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyByRegion/{regionName}.tif', 'KEEP_RESOLUTION' : False,\
          'MASK' : f'E:/GIS/Data/Raster/ScriptOutdir/Vektor/ProtMaskNollBf/{prct}.shp', 'MULTITHREADING' : False,\
           'NODATA' : None, 'OPTIONS' : 'COMPRESS=PACKBITS', 'OUTPUT' : f'E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyRegionProt/{regionName}__{prct}.tif', \
           'SET_RESOLUTION' : False, 'SOURCE_CRS' : None, 'TARGET_CRS' : None, 'X_RESOLUTION' : None, 'Y_RESOLUTION' : None }
        processing.run("gdal:cliprasterbymasklayer", param)