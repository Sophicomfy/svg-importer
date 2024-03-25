import ast
from GlyphsApp import Glyphs, GSGlyph, GSLayer, GSNode, GSPath
from AppKit import NSPoint

def create_unique_layer_name(glyph, base_name="Amicus"):
    existing_layer_names = [layer.name for layer in glyph.layers]
    if base_name not in existing_layer_names:
        return base_name
    else:
        i = 2
        while f"{base_name} {i}" in existing_layer_names:
            i += 1
        return f"{base_name} {i}"

def distribute_converted_data(converted_data):
    font = Glyphs.font
    for data_item in converted_data:
        glyph_name = data_item['glyphname']
        glyph = font.glyphs[glyph_name]

        if not glyph:
            glyph = GSGlyph(glyph_name)
            font.glyphs.append(glyph)

        new_layer_name = create_unique_layer_name(glyph, "Amicus")
        new_layer = GSLayer()
        new_layer.name = new_layer_name
        glyph.layers.append(new_layer)

        for shape in data_item['layers'][0]['shapes']:
            new_path = GSPath()
            for node_str in shape['nodes']:
                node_data = ast.literal_eval(node_str)
                x, y, node_type = node_data
                x, y = float(x), float(y)  # Convert to floats
                new_node = GSNode(NSPoint(x, y), type=node_type)
                new_path.nodes.append(new_node)
            new_path.closed = shape['closed'] == 1
            new_layer.paths.append(new_path)

    font.save()