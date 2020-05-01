parent = iface.mainWindow()

sStr, bOK = QInputDialog.getText(parent, "Title", "Prompt", text="Default")
if bOK:
    print("User entered: {}".format(sStr))
else:
    print("User: Canceled!")

iInt, bOK = QInputDialog.getInt(parent, "Title", "Prompt", 7, 1, 10, 1)
if bOK:
    print(iInt)
else:
    print("Canceled!")

dDbl, bOK = QInputDialog.getDouble(parent, "Title", "Prompt", 7.5, 1, 10, 2)
if bOK:
    print(dDbl)
else:
    print("Canceled!")

lSpecies = ['RTHA', 'SWHA', 'BTHA', 'HAHA']
sStr, bOK = QInputDialog.getItem(parent, "Species of Hawk", "What species did you see?", lSpecies, editable=False)
if bOK:
    print(sStr)
else:
    print("Canceled!")

