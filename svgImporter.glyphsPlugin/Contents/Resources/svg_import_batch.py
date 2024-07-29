from GlyphsApp import Glyphs
from svg_import_single import SVGImportLoader
from svg_import_parser import parse_glyph_name
from svg_import_distributor import convert_svg_to_glyphs_layer, distribute_data

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