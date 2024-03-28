from GlyphsApp import Glyphs
from svg_import_converter import convert_svg_to_glyphs_path

def selective_import_svg(file_path):
    layer = convert_svg_to_glyphs_path(file_path)
    Glyphs.font.selectedLayers[0].parent.layers.append(layer)
    print(f"SVG from {file_path} imported successfully.")

def batch_import_svgs(folder_path):
    from svg_import_batcher import batch_process_svgs
    batch_process_svgs(folder_path)