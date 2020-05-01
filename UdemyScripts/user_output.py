parent = iface.mainWindow()
res = QMessageBox.warning(parent, "Title of Box", "Message")
print("Result: {}".format(res))

sMsg = "QMessageBox.Cancel\n"
sMsg += "QMessageBox.Ok\n"
sMsg += "QMessageBox.Help\n"
sMsg += "QMessageBox.Open\n"
sMsg += "QMessageBox.Save\n"
sMsg += "QMessageBox.SaveAll\n"
sMsg += "QMessageBox.Discard\n"
sMsg += "QMessageBox.Close\n"
sMsg += "QMessageBox.Apply\n"
sMsg += "QMessageBox.Reset\n"
sMsg += "QMessageBox.Yes\n"
sMsg += "QMessageBox.YesToAll\n"
sMsg += "QMessageBox.No\n"
sMsg += "QMessageBox.NoToAll\n"
sMsg += "QMessageBox.NoButton\n"
sMsg += "QMessageBox.RestoreDefaults\n"
sMsg += "QMessageBox.Abort\n"
sMsg += "QMessageBox.Retry\n"
sMsg += "QMessageBox.Ignore"
res = QMessageBox.about(parent, "QMessageBox Standard Buttons", sMsg)
print("Result: {}".format(res))

while res != QMessageBox.Cancel:
    res = QMessageBox.information(parent, "Title of Box", "Message", QMessageBox.Cancel | QMessageBox.Ok | QMessageBox.Help | QMessageBox.Open | QMessageBox.Save | QMessageBox.SaveAll | QMessageBox.Discard | QMessageBox.Close | QMessageBox.Apply | QMessageBox.Reset | QMessageBox.Yes | QMessageBox.YesToAll | QMessageBox.No | QMessageBox.NoToAll | QMessageBox.NoButton | QMessageBox.RestoreDefaults | QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore, QMessageBox.Cancel)
    print("Result: {}".format(res))

res = QMessageBox.critical(parent, "Title of Box", "Message")
print("Result: {}".format(res))

res = QMessageBox.question(parent, "Title of Box", "Message")
print("Result: {}".format(res))

iface.messageBar().pushMessage("Woohoo", "It worked!!!", level=Qgis.Success)
iface.messageBar().pushMessage("Just to let you know", "Still working....", level=Qgis.Info, duration=5)
iface.messageBar().pushMessage("Oops", "Not sure if you wanted to do that", level=Qgis.Warning, duration=1)
iface.messageBar().pushMessage("Crap", "That won't work", level=Qgis.Critical)

res = QMessageBox.question(parent, "Title of Box", "Show your message in the the status bar")
if res == QMessageBox.Yes:
    iface.mainWindow().statusBar().showMessage("Your Message Here")