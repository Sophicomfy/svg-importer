font = Glyphs.font

for glyph in font.glyphs:
    for layer in glyph.layers:
        for path in layer.paths:
            layer.cleanUpPaths()
