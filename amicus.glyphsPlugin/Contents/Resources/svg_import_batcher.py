from svg_import_loader import SVGImportLoader
from svg_import_converter import convert_svg_to_glyphs_path
from GlyphsApp import Glyphs

def batch_process_svgs(folder_path):
    loader = SVGImportLoader()
    svg_files = loader.load_svg_files_from_folder(folder_path)
    for svg_file in svg_files:
        layer = convert_svg_to_glyphs_path(svg_file)
        glyph_name = derive_glyph_name_from_file_name(svg_file)
        glyph = Glyphs.font.glyphs[glyph_name] or Glyphs.font.glyphs.append(GSGlyph(glyph_name))
        glyph.layers.append(layer)
        print(f"SVG from {svg_file} imported into glyph {glyph_name}.")
