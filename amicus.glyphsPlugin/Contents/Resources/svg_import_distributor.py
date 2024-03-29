import GlyphsApp
from GlyphsApp import Glyphs, GSGlyph
from svg_import_parser import parse_glyph_name
from svg_import_converter import convert_svg_to_glyphs_layer

def distribute_data(svg_file_path):
    font = Glyphs.font
    glyph_name = parse_glyph_name(svg_file_path)
    
    # Check if glyph exists, if not create a new one
    glyph = font.glyphs[glyph_name]
    if not glyph:
        glyph = GlyphsApp.GSGlyph(glyph_name)
        glyph.name = glyph_name
        font.glyphs.append(glyph)
    
    # Convert the SVG file to a Glyphs layer
    new_layer = convert_svg_to_glyphs_layer(svg_file_path)
    if new_layer:
        # Append the new layer with a higher number
        existing_layer_numbers = [l.layerId for l in glyph.layers]
        max_layer_number = max(existing_layer_numbers) if existing_layer_numbers else 0
        new_layer_number = max_layer_number + 1
        new_layer.layerId = new_layer_number
        glyph.layers.append(new_layer)
        
        print(f"SVG from {svg_file_path} has been imported into glyph '{glyph_name}' with layer number {new_layer_number}.")
    else:
        print(f"Failed to convert SVG file: {svg_file_path}")
