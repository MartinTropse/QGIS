import os 

lyr=QgsProject.instance().mapLayersByName('Natura_2000_Dissolved')

layerList = ['NR_DiffLand', 'NP_DiffLand','Natura_2000_Dissolved','OBO_DiffLand']

for layer in layerList:
    lyr = QgsProject.instance().mapLayersByName(layer)[0]
    lyrExtent=lyr.extent()
    xMax = str(lyrExtent.xMaximum())
    xMin = str(lyrExtent.xMinimum())
    yMin = str(lyrExtent.yMinimum())
    yMax = str(lyrExtent.yMaximum())
    gdalCommand=f'gdal_rasterize -l {layer} -burn 1.0 -tr 10.0 10.0 -a_nodata 0.0 -te {xMin} {yMin} {xMax} {yMax} -ot Byte -of GTiff -co COMPRESS=PACKBITS E:/GIS/Data/Vektor/SkyddadNaturData/Edit/{layer}.shp E:/GIS/Data/Vektor/SkyddadNaturData/Edit/{layer}.tif'
    os.system(gdalCommand)


"""
    gdalCommand=f'gdal_rasterize -l {layer} -burn 1.0 -tr 10.0 10.0 -a_nodata 0.0 -te 208495.6561 6097483.2831 920451.7116 7671055.9534 -ot Byte -of GTiff -co COMPRESS=PACKBITS E:/GIS/Data/Vektor/SkyddadNaturData/Edit/{layer}.shp E:/GIS/Data/Vektor/SkyddadNaturData/Edit/{layer}.tif'
    print(gdalCommand)
"""

#gdal_rasterize -l Natura_2000_Dissolved -burn 1.0 -tr 10.0 10.0 -a_nodata 0.0 -te 208495.6561 6097483.2831 920451.7116 7671055.9534 -ot Byte -of GTiff -co COMPRESS=PACKBITS E:\GIS\Data\Vektor\SkyddadNaturData\Edit\Natura_2000_Dissolved.shp E:/GIS/Data/Vektor/SkyddadNaturData/Edit/Natura_2000.tif