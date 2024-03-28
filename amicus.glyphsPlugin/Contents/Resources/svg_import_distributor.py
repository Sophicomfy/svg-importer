import GlyphsApp
from svg_import_parser import parse_glyph_name
from svg_import_converter import convert_svg_to_glyphs_path

def distribute_data(svg_file_path):
    font = Glyphs.font
    glyph_name = parse_glyph_name(svg_file_path)
    
    glyph = font.glyphs[glyph_name]
    if not glyph:
        glyph = GSGlyph(glyph_name)
        font.glyphs.append(glyph)
    
    new_layer = convert_svg_to_glyphs_path(svg_file_path)
    glyph.layers.append(new_layer)
    
    print(f"SVG from {svg_file_path} has been imported into glyph '{glyph_name}'.")
