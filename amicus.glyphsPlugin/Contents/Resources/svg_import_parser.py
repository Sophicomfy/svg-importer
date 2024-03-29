import xml.etree.ElementTree as ET

def parse_glyph_name(svg_path):
    file_name = svg_path.split('/')[-1]
    if '_refined.svg' in file_name:
        glyph_name = file_name.replace('_refined.svg', '')
    else:
        glyph_name = file_name.replace('.svg', '')
    print("Parsed Glyph Name:", glyph_name)
    return glyph_name