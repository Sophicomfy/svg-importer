from GlyphsApp import GSSVGtoPath

def convert_svg_to_glyphs_path(svg_file_path):
    with open(svg_file_path, 'r') as svg_file:
        svg_content = svg_file.read()
    glyphs_path = GSSVGtoPath(svg_content)
    print(glyphs_path)
    return glyphs_path