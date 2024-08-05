def correct_paths_directions(font):
    for glyph in font.glyphs:
        for layer in glyph.layers:
            layer.correctPathDirections()
