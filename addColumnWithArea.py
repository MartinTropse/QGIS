#Script that adds area field
#Could easily be expanded to be applied to multiple layers simulationously, using mc.layers() and creating a outloop of layers. 

layer = iface.activeLayer()
provider = layer.dataProvider()

areas = [ feat.geometry().area() 
          for feat in layer.getFeatures() ]

field = QgsField("area", QVariant.Double)
provider.addAttributes([field])
layer.updateFields()

idx = layer.fieldNameIndex('area')

for area in areas:
    new_values = {idx : float(area)}
    provider.changeAttributeValues({areas.index(area):new_values})