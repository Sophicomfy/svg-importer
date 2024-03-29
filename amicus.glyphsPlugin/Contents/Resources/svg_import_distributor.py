import GlyphsApp
from GlyphsApp import Glyphs, GSGlyph
from svg_import_converter import convert_svg_to_glyphs_layer
from svg_import_parser import parse_glyph_name

def distribute_data(svg_file_path):
    font = Glyphs.font  # Access the current font
    glyph_name = parse_glyph_name(svg_file_path)  # Correctly parse the glyph name from the SVG file
    
    # Find or create glyph
    glyph = font.glyphs[glyph_name]
    if not glyph:
        glyph = GlyphsApp.GSGlyph(glyph_name)
        glyph.name = glyph_name
        font.glyphs.append(glyph)
        glyph = font.glyphs[glyph_name]
    
    # Convert SVG file to a Glyphs layer
    new_layer = convert_svg_to_glyphs_layer(svg_file_path)
    if new_layer:
        # Name the new layer appropriately
        iteration_number = len(glyph.layers)
        new_layer.name = f"imported_svg_{iteration_number}"
        glyph.layers.append(new_layer)
        print(f"SVG from {svg_file_path} has been imported into glyph '{glyph_name}' with layer named '{new_layer.name}'.")
    else:
        print(f"Failed to convert SVG file: {svg_file_path}")

        print(f"Failed to convert SVG file: {svg_file_path}")

