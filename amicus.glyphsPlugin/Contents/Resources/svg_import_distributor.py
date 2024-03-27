import GlyphsApp

def distribute_data(glyphs_file, parsed_data):
    font = Glyphs.font

    for data_item in parsed_data:
        glyph_name = data_item['glyph_name']
        shapes_data = data_item['shapes']

        glyph = font.glyphs[glyph_name]
        if not glyph:
            glyph = GSGlyph(glyph_name)
            font.glyphs.append(glyph)
        
        import_layers = [layer for layer in glyph.layers if layer.name.startswith("import")]
        next_import_number = len(import_layers) + 1
        layer_name = f"import{next_import_number:02d}"

        new_layer = GSLayer()
        new_layer.name = layer_name
        glyph.layers.append(new_layer)
        
        new_layer.shapes = shapes_data
        
        print(f"Data distributed into glyph '{glyph_name}' on layer '{layer_name}'.")

    font.save()