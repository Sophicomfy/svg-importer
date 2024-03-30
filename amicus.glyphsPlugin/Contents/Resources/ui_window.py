from GlyphsApp import Glyphs, GetOpenFile, GetFolder
from vanilla import Window, Button, TextBox
from svg_import_loader import SVGImportLoader
from svg_import_distributor import distribute_data
from svg_import import batch_import_svgs, selective_import_svg

class AmicusWindow:
    def __init__(self):
        self.w = Window((400, 160), "Amicus SVG Importer")
        self.w.text = TextBox((15, 12, -15, 17), "Choose import option:", sizeStyle='small')
        self.w.selectiveImportButton = Button((15, 40, 180, 20), "Selective Import", callback=self.selectiveImportCallback)
        self.w.batchImportButton = Button((15, 70, 180, 20), "Batch Import", callback=self.batchImportCallback)
        self.w.cancelButton = Button((15, 100, 180, 20), "Cancel", callback=self.closeWindow)
        self.w.open()

    def selectiveImportCallback(self, sender):
        filePath = GetOpenFile("Select an SVG file")
        if filePath:
            distribute_data(filePath)

    def batchImportCallback(self, sender):
        folderPath = GetFolder("Select a folder containing SVG files")
        if folderPath:
            batch_import_svgs(folderPath)

    def closeWindow(self, sender):
        self.w.close()
