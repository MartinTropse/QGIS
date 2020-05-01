#Extract raster statistics from all rasters in a folder

import os
import panas

path="E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SymphonyRegionTotalprot"
dirList=os.listdir(path) #Can easily be expanded to a os.walk script
print(dirList)

df=pd.DataFrame()

nameList = []
meanList = []
rangeList = []
sdList = []
sumList = []
geoList = []

for tif in dirList:
    if tif.endswith(".tif"):
        tifLayer = QgsRasterLayer(path+"/"+tif, "GreatTif")
        if tifLayer.isValid():
            stats=tifLayer.dataProvider().bandStatistics(1, QgsRasterBandStats.all)
            nameList.append(tif)
            meanList.append(stats.mean)
            rangeList.append(stats.range)
            sdList.append(stats.stdDev)
            sumList.append(stats.sum)
            geoList.append(tifLayer.geometry().area())
        else:
            print("This one has an issue: {tif} :o")
            
print("All done sir!")

df['Name'] = nameList
df['Mean'] = meanList
df['Range'] = rangeList
df['Sd'] = sdList
df['Sum'] = sumList

df.to_csv("E:/GIS/Data/Raster/Symphony/AnalysFold/250m/SympRegProt_Stats.csv", encoding='latin-1')