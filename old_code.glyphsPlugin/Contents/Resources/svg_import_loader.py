# svg_import_loader.py
import os

class SVGImportLoader:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def load_svg_files(self):
        svg_files = [os.path.join(self.root_dir, f) for f in os.listdir(self.root_dir) if f.endswith("_refined.svg")]
        return svg_files