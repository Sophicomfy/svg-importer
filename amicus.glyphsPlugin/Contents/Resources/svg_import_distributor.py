from GlyphsApp import Glyphs, GSGlyph, GSLayer, GSPath, GSNode

def distribute_converted_data(converted_data):
    font = Glyphs.font  # Current font opened in Glyphs

    for data_item in converted_data:
        glyph_name = data_item["glyphname"]
        glyph = font.glyphs[glyph_name]

        # Check if glyph exists, if not, create it
        if not glyph:
            glyph = GSGlyph(glyph_name)
            font.glyphs.append(glyph)

        # Create new layer for the glyph
        new_layer = GSLayer()
        new_layer.layerId = data_item["layers"][0]["layerId"]
        new_layer.width = data_item["layers"][0]["width"]
        glyph.layers.append(new_layer)

        # Draw paths from the converted data into the new layer
        for shape in data_item["layers"][0]["shapes"]:
            new_path = GSPath()
            for node_data in shape["nodes"]:
                x, y, node_type = node_data
                node_type = 'LINE' if node_type == 'l' else 'CURVE' if node_type == 'c' else 'OFFCURVE'
                new_node = GSNode(NSPoint(x, y), type=node_type)
                new_path.nodes.append(new_node)
            new_path.closed = True if shape["closed"] == 1 else False
            new_layer.paths.append(new_path)

        if "unicode" in data_item:
            glyph.unicode = data_item["unicode"]

    font.save()


distribute_converted_data(converted_data)
