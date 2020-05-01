#Cut raster by vector through cmd. Also utilize layerTreeRoot and iterates through specific "children/groups" 


import os

root=QgsProject.instance().layerTreeRoot()

for group in root.children():
    print(group.name())
    if group.name() == "RegionVektor":
        RV_Group = group
    if group.name() == "Symphony250Swerf":
        S250_Group = group

for child in S250_Group.children():
    SympName=child.name()
    for newChild in RV_Group.children():
        RegionName = newChild.name()
        gdal_command=f'gdalwarp -of GTiff -cutline E:/GIS/Data/Raster/ScriptOutdir/Vektor/NollBf/{RegionName}.shp -cl {RegionName} \
        -crop_to_cutline -co COMPRESS=PACKBITS E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SweRef99/{SympName}.tif E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyByRegion/{SympName}{RegionName}.tif'
        os.system(gdal_command)