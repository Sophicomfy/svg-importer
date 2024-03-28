import xml.etree.ElementTree as ET

def parse_glyph_name(svg_path):
    glyph_name = svg_path.split('/')[-1].replace('_refined.svg', '')
    print("Parsed Glyph Name")
    print(glyph_name)
    return glyph_name