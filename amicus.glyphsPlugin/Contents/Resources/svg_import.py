from GlyphsApp import Glyphs
from svg_import_loader import SVGImportLoader
from svg_import_parser import parse_glyph_name
from svg_import_converter import convert_svg_to_glyphs_layer
from svg_import_distributor import distribute_layer_to_glyph
from svg_import_batcher import batch_process_svgs

def selective_import_svg(file_path):
    layer = convert_svg_to_glyphs_layer(file_path)
    Glyphs.font.selectedLayers[0].parent.layers.append(layer.shapes[0])
    print(f"SVG from {file_path} imported successfully.")

def batch_import_svgs(folder_path):
    batch_process_svgs(folder_path)
    print(f"Batch import completed for SVG files in {folder_path}")
