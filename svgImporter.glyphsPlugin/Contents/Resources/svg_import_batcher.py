from GlyphsApp import Glyphs
from svg_import_loader import SVGImportLoader
from svg_import_parser import parse_glyph_name
from svg_import_converter import convert_svg_to_glyphs_layer
from svg_import_distributor import distribute_data

def batch_process_svgs(folder_path):
    loader = SVGImportLoader()
    svg_files = loader.load_svg_files_from_folder(folder_path)
    for svg_file in svg_files:
        glyph_name = parse_glyph_name(svg_file)  
        layer = convert_svg_to_glyphs_layer(svg_file)
        if layer:
            distribute_data(svg_file)
            print(f"Successfully imported {svg_file} into '{glyph_name}'.")
            Glyphs.font.save() 
            print("File saved")
        else:
            print(f"Conversion failed for {svg_file}. Skipping...")