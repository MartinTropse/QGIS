import os
from osgeo import gdal, ogr
import time


def ClipRasterWithPolygon(rasterPath, polyPath, outPath):
    os.system("gdalwarp -dstnodata -9999 -q -cutline " + polyPath + " -crop_to_cutline " + " -of GTiff "+ rasterPath + " " + outPath)
    
def CreateClippingPolygon(inPath, field):
    driverSHP = ogr.GetDriverByName("ESRI Shapefile")
    ds = driverSHP.Open(inPath)
    if ds is None:
        print('layer not open')
    lyr = ds.GetLayer()
    spatialRef = lyr.GetSpatialRef()
    
    for feature in lyr:
        fieldVal = feature.GetField(field)
        os.mkdir("ClippingFeatures/"+str(fieldVal))
        outds = driverSHP.CreateDataSource("ClippingFeatures/"+str(fieldVal)+"/clip.shp")
        outlyr = outds.CreateLayer(str(fieldVal)+"/clip.shp", srs=spatialRef, geom_type=ogr.wkbPolygon)
        outDfn = outlyr.GetLayerDefn()
        ingeom = feature.GetGeometryRef()       
        outFeat = ogr.Feature(outDfn)
        outFeat.SetGeometry(ingeom)
        outlyr.CreateFeature(outFeat) 
        
def ClipRasters(inPath, field):
    driverSHP = ogr.GetDriverByName("ESRI Shapefile")
    ds = driverSHP.Open(inPath)
    if ds is None:
        print("Layer not open")
    lyr = ds.GetLayer()
    
    for feature in lyr:
        fieldVal = feature.GetField(field)
        ClipRasterWithPolygon("E:/GIS/Data/Raster/NMD_Hav.tif", "ClippingFeatures/"+str(fieldVal), "ClippingFeatures/"+str(fieldVal+"/dem.tif"))
        print("Cutting out raster"+str(fieldVal)+" any moment now!")

#Run
os.chdir("D:/GIS/QGIS")
os.makedirs("ClippingFeatures", exist_ok=True) 

CreateClippingPolygon("E:\GIS\Data\Vektor\HaV_Skyddadeomraden\HavLand.shp", "LANSNAMN")
print("\nWe got here")
time.sleep(5)

ClipRasters("E:/GIS/Data/Vektor/HaV_Skyddadeomraden/HavLand.shp", "LANSNAMN")

print("Operation complete!")