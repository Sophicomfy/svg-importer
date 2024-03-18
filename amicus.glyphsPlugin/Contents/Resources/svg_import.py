# svg_import.py
from GlyphsApp import GetOpenFile, GetFolder
from svg_import_loader import SVGImportLoader

def batch_import_svg():
    folder_path = GetFolder("Select the folder containing 'refined.svg' files")
    if folder_path:
        loader = SVGImportLoader()
        loader.load_svg_files_from_folder(folder_path)
    else:
        print("Batch import cancelled. No folder was selected.")

def selective_import_svg():
    file_path = GetOpenFile("Select an SVG file")
    if file_path:
        loader = SVGImportLoader()
        loader.load_single_svg(file_path)
    else:
        print("Selective import cancelled. No SVG file was selected.")