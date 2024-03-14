# svg_import.py
from GlyphsApp import *
from svg_import_loader import SVGImportLoader
from svg_import_parser import parse_svg

def batch_import_svg():
    folder_path = GetFolder(message="Select the folder containing 'refined.svg' files")
    if folder_path:
        loader = SVGImportLoader(folder_path)
        svg_files = loader.load_svg_files()
        svg_data = [parse_svg(file_path) for file_path in svg_files if parse_svg(file_path) is not None]

        # Enhanced printing for verification
        for data in svg_data:
            print(f"Glyph Name: {data['glyph_name']}, Char Index: {data['char_index']}, Paths:")
            for path in data['paths']:
                print(f"    Path: {path}")
        print(f"Loaded and parsed {len(svg_data)} SVG files from {folder_path}.")
    else:
        print("No folder was selected.")