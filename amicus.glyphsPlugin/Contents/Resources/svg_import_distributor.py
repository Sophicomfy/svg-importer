from GlyphsApp import Glyphs, GSGlyph, GSLayer, GSNode
from AppKit import NSPoint

def create_unique_layer_name(glyph, base_name="Amicus"):
    if glyph.layers[base_name]:  # Check if base layer name exists.
        i = 2
        while glyph.layers[f"{base_name} {i}"]:  # Increment i until a unique name is found.
            i += 1
        return f"{base_name} {i}"
    else:
        return base_name

def distribute_converted_data(converted_data):
    font = Glyphs.font  # Access the currently open font in Glyphs.

    for data_item in converted_data:
        glyph_name = data_item['glyphname']

        # Check if glyph exists, if not, create it
        glyph = font.glyphs[glyph_name]
        if not glyph:
            glyph = GSGlyph(glyph_name)
            font.glyphs.append(glyph)
        
        # Generate a unique layer name and create the layer
        new_layer_name = create_unique_layer_name(glyph, "Amicus")
        new_layer = GSLayer()
        new_layer.name = new_layer_name
        glyph.layers.append(new_layer)

        # Assign converted shapes to the new layer
        for shape in data_item['layers'][0]['shapes']:
            new_path = GSPath()
            for node_data in shape['nodes']:
                # Create and append new nodes to the path
                new_node = GSNode(NSPoint(*node_data[:2]), type=node_data[2])
                new_path.nodes.append(new_node)
            new_path.closed = shape['closed'] == 1
            new_layer.paths.append(new_path)

    print("All converted data have been distributed into respective glyphs.")
    font.save()  # Save the font with all updates.
