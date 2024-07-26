import os
import sys
import logging

class SVGImportLoader:
    def __init__(self):
        self.loaded_files = []
        self.name_mappings_content = ""

    def log(self, message):
        sys.stdout.write(f"[SVGImportLoader] {message}\n")
        sys.stdout.flush()

    def load_single_svg(self, file_path):
        self.log(f"Attempting to load single SVG: {file_path}")
        if file_path.endswith(".svg"):
            self.loaded_files.append(file_path)
            self.log(f"Successfully loaded: {file_path}")
            return file_path
        else:
            self.log("Selected file is not an SVG.")
            return None

    def load_svg_files_from_folder(self, folder_path):
        self.log(f"Loading SVG files from folder: {folder_path}")
        svg_files = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith("_refined.svg"):
                full_path = os.path.join(folder_path, file_name)
                svg_files.append(full_path)
                self.log(f"Loaded SVG file: {full_path}")
        svg_files.sort()
        if not svg_files:
            self.log(f"No SVG files found in {folder_path}.")
        return svg_files

    def load_name_mappings(self, folder_path):
        self.log(f"Loading name mappings from folder: {folder_path}")
        mappings_file_path = os.path.join(folder_path, "_name_mappings.txt")
        try:
            with open(mappings_file_path, 'r') as file:
                self.name_mappings_content = file.read()
        except FileNotFoundError:
            self.log(f"Name mappings file not found at {mappings_file_path}. Using default names.")
        except Exception as e:
            self.log(f"Error loading name mappings: {e}. Using default names.")

        self.log(f"Name mappings content: {self.name_mappings_content}")
        return self.name_mappings_content