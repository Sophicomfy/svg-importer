# ui_window.py
from vanilla import Window, Button, TextBox
from svg_import import batch_import_svg

class AmicusWindow:
    def __init__(self):
        self.w = Window((400, 160), "Amicus SVG Importer")

        self.w.text = TextBox((15, 12, -15, 17), "SVG Import Options", sizeStyle='small')

        self.w.batchImportButton = Button((15, 40, 180, 20), "Batch Import", callback=self.batchImportCallback)
        self.w.selectiveImportButton = Button((15, 70, 180, 20), "Selective Import", callback=self.dummyCallback)
        self.w.cancelButton = Button((15, 100, 180, 20), "Cancel", callback=self.closeWindow)

        self.w.open()

    def dummyCallback(self, sender):
        print("This is a dummy callback.")

    def batchImportCallback(self, sender):
        batch_import_svg()

    def closeWindow(self, sender):
        self.w.close()

if __name__ == "__main__":
    AmicusWindow()
