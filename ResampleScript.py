# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:14:34 2020
@author: MartinTropse
"""

#Script to resample all tif-files to 10*10 raster. 

import os
import time
import re

pattern = re.compile("\.tif$")

for dirc, subdir, files in os.walk("D:/GIS/Data/Raster/Symphony/National_eco_E_2018"):
    for file in files:
        a=re.search(pattern, file)
        if a:
            print(f"Woaw it looks like a file {file}")
            processing.run("grass7:r.resample", {'input':f'D:/GIS/Data/Raster/Symphony/National_eco_E_2018/{file}','output':f'D:/GIS/Data/Raster/Symphony/National_eco_E_2018/10m_{file}','GRASS_REGION_PARAMETER':None,'GRASS_REGION_CELLSIZE_PARAMETER':10,'GRASS_RASTER_FORMAT_OPT':'','GRASS_RASTER_FORMAT_META':''})
print("I be damn, we made it!")
print("It is true!")    