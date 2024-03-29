from GlyphsApp import Glyphs
from svg_import_loader import SVGImportLoader
from svg_import_converter import convert_svg_to_glyphs_path
from svg_import_batcher import batch_process_svgs

def selective_import_svg(file_path):
    layer = convert_svg_to_glyphs_layer(file_path)
    Glyphs.font.selectedLayers[0].parent.layers.append(layer.shapes[0])
    print(f"SVG from {file_path} imported successfully.")

def batch_import_svgs(folder_path):
    loader = SVGImportLoader()
    svg_files = loader.load_svg_files_from_folder(folder_path)
    for svg_file in svg_files:
        layer = convert_svg_to_glyphs_path(svg_file)
        glyph_name = derive_glyph_name_from_file_name(svg_file)
        glyph = Glyphs.font.glyphs[glyph_name] or Glyphs.font.glyphs.append(GSGlyph(glyph_name))
        glyph.layers.append(layer)
        print(f"SVG from {svg_file} imported into glyph {glyph_name}.")
