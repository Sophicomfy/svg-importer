# svg_import.py
import os
from vanilla import FileDialog
from svg_import_loader import SVGImportLoader

def batch_import_svg():
    folder_path = FileDialog.getFolder()
    if folder_path:
        loader = SVGImportLoader(folder_path)
        svg_files = loader.load_svg_files()
        # Placeholder for further processing of loaded SVG files
        print(f"Loaded {len(svg_files)} SVG files from {folder_path}.")