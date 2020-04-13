import os
from osgeo import gdal, ogr
import re
import sys

#pattern=re.compile(r"Skyddade[a-zA-Z]+\.tif$")
pattern=re.compile(r"Hav\.tif$")

for dirc, subdirc, files in os.walk(r"E:\GIS\Data\Raster\Jobbdator_Lager\HavRegioner"):
    for file in files:
        srch = re.search(pattern, file)
        if srch:
            inFile=dirc+"\\"+file
            outFile=dirc+"\\"+"SummaryRegStat.html"
            processing.run("qgis:rasterlayerstatistics", {'INPUT':inFile,'BAND':1,'OUTPUT_HTML_FILE':outFile})
print("Made it!")