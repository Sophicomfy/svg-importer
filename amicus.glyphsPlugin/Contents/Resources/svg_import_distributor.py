import GlyphsApp
from GlyphsApp import Glyphs, GSGlyph
from svg_import_parser import parse_glyph_name
from svg_import_converter import convert_svg_to_glyphs_layer

import GlyphsApp
from svg_import_converter import convert_svg_to_glyphs_layer

def distribute_data(svg_file_path):
    font = Glyphs.font  # Access the current font
    glyph_name = "yourGlyphName"  # This should be replaced with actual logic to extract glyph name
    
    # Find or create glyph
    glyph = font.glyphs[glyph_name]
    if not glyph:
        glyph = GlyphsApp.GSGlyph(glyph_name)
        font.glyphs.append(glyph)
        glyph = font.glyphs[glyph_name]
    
    # Convert SVG file to a Glyphs layer
    new_layer = convert_svg_to_glyphs_layer(svg_file_path)
    if new_layer:
        glyph.layers.append(new_layer)
        print(f"SVG from {svg_file_path} has been imported into glyph '{glyph_name}'.")
    else:
        print(f"Failed to convert SVG file: {svg_file_path}")

