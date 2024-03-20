# svg_import.py
from GlyphsApp import GetOpenFile, GetFolder
from svg_import_loader import SVGImportLoader
from svg_import_batcher import batch_process_svgs
from svg_import_parser import parse_svg

def selective_import_svg():
    file_path = GetOpenFile("Select an SVG file")
    if file_path:
        loader = SVGImportLoader()
        loaded_file = loader.load_single_svg(file_path)
        if loaded_file:
            parse_svg(loaded_file, print_parsed_data=True)
        else:
            print("Failed to load the SVG file.")
    else:
        print("Selective import cancelled. No SVG file was selected.")

def batch_import_svg():
    folder_path = GetFolder("Select the folder containing 'refined.svg' files")
    if folder_path:
        batch_process_svgs(folder_path)
    else:
        print("Batch import cancelled. No folder was selected.")