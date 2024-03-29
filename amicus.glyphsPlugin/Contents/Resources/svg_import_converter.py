from GlyphsApp import GSSVGtoPath

def convert_svg_to_glyphs_path(svg_file_path):
    # Directly pass the file path to GSSVGtoPath
    layer = GSSVGtoPath(svg_file_path)
    print(layer)
    return layer