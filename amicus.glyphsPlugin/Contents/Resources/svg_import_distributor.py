import GlyphsApp
from svg_import_parser import parse_svg
from svg_import_converter import construct_glyphs_shapes

def distribute_data(font, converted_data):
    for data_item in converted_data:
        glyph_name = data_item['glyph_name']
        shapes_data = data_item['shapes']
        
        glyph = font.glyphs[glyph_name]
        if not glyph:
            glyph = GSGlyph(glyph_name)
            font.glyphs.append(glyph)

        import_layers = [layer for layer in glyph.layers if layer.name.startswith("import")]
        number_of_imported_layers = len(import_layers) + 1
        layer_name = "import" + str(number_of_imported_layers).zfill(2)

        new_layer = GSLayer()
        new_layer.name = layer_name
        glyph.layers.append(new_layer)

        new_layer.shapes = eval(shapes_data)

        print(f"Data distributed into glyph '{glyph_name}' on layer '{layer_name}'.")
    font.save()