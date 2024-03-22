from GlyphsApp import Glyphs

def distribute_converted_data(converted_data):
    font = Glyphs.font  # Current font opened in Glyphs

    for data_item in converted_data:
        glyph_name = data_item["glyphname"]
        glyph = font.glyphs[glyph_name]

        if not glyph:
            glyph = GSGlyph(glyph_name)
            font.glyphs.append(glyph)
        
        new_layer = GSLayer()
        new_layer.layerId = data_item["layers"][0]["layerId"]
        new_layer.width = data_item["layers"][0]["width"]
        glyph.layers.append(new_layer)

        for shape in data_item["layers"][0]["shapes"]:
            new_path = GSPath()
            for node_data in shape["nodes"]:
                x, y, node_type = node_data
                new_node = GSNode((x, y), type=node_type)
                new_path.nodes.append(new_node)
            new_path.closed = shape["closed"]
            new_layer.paths.append(new_path)

        glyph.unicode = data_item["unicode"]

    font.save()