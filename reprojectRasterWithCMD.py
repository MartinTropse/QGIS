#Command to reproject raster files add compressing them with LZW 

import os
import re

pattern=re.compile(r".+\.tif$")
files=os.listdir("C:/GIS/CurrentDirectory/AnalysFold/10m")

for file in files:
	check = re.search(pattern, file)
	if check:
		gdal_command=f"gdalwarp -s_srs IGNF:ETRS89LAEA -t_srs EPSG:3006 -tr 10.0 10.0 -r near -of GTiff -co COMPRESS=LZW C:/GIS/CurrentDirectory/AnalysFold/10m/{file} C:/GIS/CurrentDirectory/AnalysFold/10m/{file[:-4]}swrf99.tif"
		os.system(gdal_command)

#gdalwarp -s_srs EPSG:3035 -t_srs EPSG:3006 -r near -of GTiff -co COMPRESS=PACKBITS C:/GIS/CurrentDirectory/AnalysFold/10m/{file} C:/GIS/CurrentDirectory/AnalysFold/10m/{file[:-4]swrf99.tif} 

#10m raster command. 
#gdal_command=f"gdalwarp -s_srs IGNF:ETRS89LAEA -t_srs EPSG:3006 -r near -of GTiff -co COMPRESS=LZW C:/GIS/CurrentDirectory/AnalysFold/10m/{file} C:/GIS/CurrentDirectory/AnalysFold/10m/{file[:-4]}swrf99.tif"