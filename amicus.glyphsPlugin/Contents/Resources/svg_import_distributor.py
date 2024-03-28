from GlyphsApp import Glyphs, GSGlyph, GSLayer
from svg_import_parser import parse_svg_file_name
from svg_import_converter import convert_svg_to_glyphs_path

def distribute_svg_to_glyph(svg_file_path):
    glyph_name = parse_svg_file_name(svg_file_path)
    layer = convert_svg_to_glyphs_path(svg_file_path)

    glyph = Glyphs.font.glyphs[glyph_name]
    if not glyph:
        glyph = GSGlyph(glyph_name)
        Glyphs.font.glyphs.append(glyph)

    # Assuming the logic to name layers based on some criteria or simply adding a new layer
    new_layer_name = "Imported SVG"
    new_layer = GSLayer()
    new_layer.name = new_layer_name
    new_layer.shapes = layer.shapes  # Copy shapes from converted layer to the new layer
    glyph.layers.append(new_layer)

    print(f"SVG from {svg_file_path} has been distributed to glyph '{glyph_name}' in layer '{new_layer_name}'.")
