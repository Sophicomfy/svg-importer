import os

class SVGImportLoader:
    def __init__(self):
        self.loaded_files = []

    def load_single_svg(self, file_path):
        if file_path.endswith(".svg"):
            self.loaded_files.append(file_path)
            print(f"Successfully loaded: {file_path}")
            return file_path
        else:
            print("Selected file is not an SVG.")
            return None

    def load_svg_files_from_folder(self, folder_path):
        svg_files = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith("_refined.svg"): # we need _refined otherwise importing bullshits
                full_path = os.path.join(folder_path, file_name)
                svg_files.append(full_path)
                print(f"Loaded SVG file: {full_path}")
        if not svg_files:
            print(f"No SVG files found in {folder_path}.")
        return svg_files
            