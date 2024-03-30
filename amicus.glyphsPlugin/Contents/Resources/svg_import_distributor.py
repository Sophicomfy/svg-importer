import GlyphsApp
from GlyphsApp import Glyphs, GSGlyph
from svg_import_converter import convert_svg_to_glyphs_layer
from svg_import_parser import parse_glyph_name, parse_layer_name

def distribute_data(svg_file_path):
    font = Glyphs.font  # Access the current font
    glyph_name = parse_glyph_name(svg_file_path)  # Parse the glyph name
    layer_name = parse_layer_name(svg_file_path)  # Parse the layer name
    
    glyph = font.glyphs[glyph_name]
    if not glyph:
        glyph = GSGlyph(glyph_name)
        glyph.name = glyph_name
        font.glyphs.append(glyph)
    
    new_layer = convert_svg_to_glyphs_layer(svg_file_path)
    if new_layer:
        new_layer.name = f"{layer_name}"  # Apply the parsed layer name directly
        glyph.layers.append(new_layer)
        print(f"SVG from {svg_file_path} imported into '{glyph_name}' with layer named '{new_layer.name}'.")
    else:
        print(f"Failed to convert SVG: {svg_file_path}")
