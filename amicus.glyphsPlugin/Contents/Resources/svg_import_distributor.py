import GlyphsApp
from GlyphsApp import Glyphs, GSGlyph, GSLayer
from svg_import_converter import convert_svg_to_glyphs_layer
from svg_import_parser import parse_glyph_name, parse_layer_name

def distribute_data(svg_file_path):
    font = Glyphs.font  # Access the current font
    glyph_name = parse_glyph_name(svg_file_path)  # Correctly parse the glyph name from the SVG file
    layer_name = parse_layer_name(svg_file_path)  # Parse the layer name
    
    glyph = font.glyphs[glyph_name]
    if not glyph:
        glyph = GSGlyph(glyph_name)
        glyph.name = glyph_name
        font.glyphs.append(glyph)
    
    new_layer = convert_svg_to_glyphs_layer(svg_file_path)

    if new_layer:
        masterLayer = glyph.layers[0]  # Assuming the first layer is the master layer
        
        # Check if the master layer is empty
        if not masterLayer.shapes:
            masterLayer.shapes.extend(new_layer.shapes)
            masterLayer.name = layer_name
            print(f"SVG from {svg_file_path} imported into master layer of '{glyph_name}'.")
        else:
            # If the master layer is not empty, create a new layer
            newLayer = GSLayer()
            newLayer.associatedMasterId = masterLayer.associatedMasterId  # Associate with the same master
            newLayer.name = layer_name
            newLayer.shapes.extend(new_layer.shapes)
            glyph.layers.append(newLayer)
            print(f"SVG from {svg_file_path} imported into new layer '{layer_name}' of '{glyph_name}'.")
    else:
        print(f"Failed to convert SVG file: {svg_file_path}")
