# svg_import.py
from GlyphsApp import GetOpenFile, GetFolder
from svg_import_loader import SVGImportLoader
from svg_import_batcher import batch_process_svgs
from svg_import_parser import parse_svg
from svg_import_converter import construct_glyphs_shapes
from svg_import_distributor import distribute_data

def selective_import_svg():
    file_path = GetOpenFile("Select an SVG file")
    if file_path:
        parsed_data = parse_svg(file_path)
        if parsed_data:
            converted_data = construct_glyphs_shapes([parsed_data])  
            distribute_data(converted_data) 
        else:
            print("Failed to parse the SVG file.")
    else:
        print("Selective import cancelled. No SVG file was selected.")


def batch_import_svg():
    folder_path = GetFolder("Select the folder containing 'refined.svg' files")
    if folder_path:
        converted_data = batch_process_svgs(folder_path)
        distribute_data(converted_data)
    else:
        print("Batch import cancelled. No folder was selected.")
