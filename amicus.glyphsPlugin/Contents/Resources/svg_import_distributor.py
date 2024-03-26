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
    font = Glyphs.font  # Access the current font
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

        # Here, directly insert shapes data as it is
        shapes_data = data_item['shapes']  # Assuming 'shapes' is a key in your data_item dictionary
        # This is the crucial part, directly inserting shapes data into the newly created layer's userData
        new_layer.userData['importedShapes'] = shapes_data

    font.save()


    