from GlyphsApp import GSGlyph, GSLayer, Glyphs
from svg_import_parser import parse_svg
from svg_import_converter import construct_glyphs_shapes

def distribute_data(glyphs_file, data):
    font = Glyphs.font

    for data_item in data:
        glyph_name, shapes_data = data_item['glyph_name'], data_item['shapes']

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

        new_layer.setUserData_forKey_(shapes_data, "importedShapesData")

        print(f"Data inserted into glyph '{glyph_name}' on layer '{layer_name}'.")

    font.save()