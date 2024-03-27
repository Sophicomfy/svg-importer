from GlyphsApp import Glyphs, GSLayer

def distribute_to_glyphs(glyph_name, shapes_data):
    font = Glyphs.font
    
    glyph = font.glyphs[glyph_name]
    if not glyph:
        glyph = GSGlyph(glyph_name)
        font.glyphs.append(glyph)
        glyph = font.glyphs[glyph_name]
    
    import_layers = [layer for layer in glyph.layers if layer.name.startswith("import")]
    if import_layers:
        highest_number = max([int(layer.name.replace("import", "")) for layer in import_layers])
        new_layer_number = highest_number + 1
    else:
        new_layer_number = 1

    new_layer_name = "import" + str(new_layer_number).zfill(2)
    new_layer = GSLayer()
    new_layer.name = new_layer_name
    glyph.layers.append(new_layer)

    new_layer.shapes = eval(shapes_data)  

    font.save()

distribute_to_glyphs(glyph_name, shapes_data)

