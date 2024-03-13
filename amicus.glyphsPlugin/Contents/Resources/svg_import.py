# svg_import.py
from GlyphsApp import *
from svg_import_loader import SVGImportLoader

def batch_import_svg():
    # Using Glyphs' method to get a folder path
    folder_path = GetFolder(message="Select the folder containing 'refined.svg' files")
    
    if folder_path:
        loader = SVGImportLoader(folder_path)
        svg_files = loader.load_svg_files()
        print(f"Loaded {len(svg_files)} SVG files from {folder_path}.")
    else:
        print("No folder was selected.")
