import os

class SVGImportLoader:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def load_svg_files(self):
        svg_files = []
        for file in os.listdir(self.root_dir):
            if file.endswith("refined.svg"):
                svg_files.append(os.path.join(self.root_dir, file))
        return svg_files
