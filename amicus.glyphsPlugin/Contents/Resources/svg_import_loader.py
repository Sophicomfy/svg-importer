# svg_import_loader.py
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
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".svg"):
                full_path = os.path.join(folder_path, file_name)
                self.loaded_files.append(full_path)
        if self.loaded_files:
            print(f"Loaded {len(self.loaded_files)} SVG files from {folder_path}.")
        else:
            print("No SVG files found in the selected folder.")