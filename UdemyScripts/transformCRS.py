crsLL = QgsCoordinateReferenceSystem(4326)
crsUTM = QgsCoordinateReferenceSystem(26914)
print("crsLL = {}".format(crsLL.description()))
print("crsUTM = {}".format(crsUTM.description()))
xf = QgsCoordinateTransform(crsLL, crsUTM, QgsProject.instance())
if xf.isValid():
    ptLL = QgsPointXY(-99.5, 19.5)
    ptUTM = xf.transform(ptLL)
    ptLL2 = xf.transform(ptUTM, QgsCoordinateTransform.ReverseTransform)
    print("LL: {}\nUTM: {}\nLL2: {}".format(ptLL.asWkt(), ptUTM.asWkt(), ptLL.asWkt()))
else:
    print("Invalid transformation")
