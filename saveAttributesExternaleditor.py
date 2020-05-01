import os
from qgis.core import QgsApplication, QgsVectorLayer

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'C:\OSGeo4W64\apps\Qt5\plugins'
os.environ['PATH'] += r';C:\OSGeo4W64\apps\qgis\bin;C:\OSGeo4W64\apps\Qt5\bin'

qgs = QgsApplication([], False)
qgs.initQgis()

data_dir="D:/GIS/QGIS/Data/ExcerciceData/QGIS-Training-Data-2.0/QGIS-Training-Data-2.0/UppsalaData"

filename = 'place.shp'
uri = os.path.join(data_dir, filename)
layer = QgsVectorLayer(uri, 'place', 'ogr')

output_name = 'output2.csv'
output_path = os.path.join(data_dir, output_name)
    
with open(output_path, 'w') as output_file:
    fieldnames = [field.name() for field in layer.fields()]
    line = ','.join(name for name in fieldnames) + '\n'
    output_file.write(line)
    for f in layer.getFeatures():
        line = ','.join(str(f[name]) for name in fieldnames) + '\n'
        output_file.write(line)

print('Success: ', 'Output file written at' + output_path)
qgs.exitQgis()
