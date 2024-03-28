# svg_import.py
from GlyphsApp import *
from svg_import_loader import SVGImportLoader
from svg_import_batcher import batch_process_svgs
from svg_import_parser import parse_svg
from svg_import_converter import construct_glyphs_shapes
from svg_import_distributor import distribute_data

def selective_import_svg():
    file_path = GetOpenFile("Select an SVG file")
    if file_path:
        # Direct conversion and adding to the current glyph
        Glyphs.font.selectedLayers[0].parent.layers.append(GSSVGtoPath(file_path))
        print(f"SVG from {file_path} imported into the current glyph.")
        
def batch_import_svg():
    folder_path = GetFolder("Select the folder containing 'refined.svg' files")
    if folder_path:
        converted_data = batch_process_svgs(folder_path)
        distribute_data(converted_data)
    else:
        print("Batch import cancelled. No folder was selected.")
