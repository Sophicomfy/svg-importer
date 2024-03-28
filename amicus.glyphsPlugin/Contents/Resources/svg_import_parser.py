import xml.etree.ElementTree as ET

def parse_glyph_name(svg_path):
    # Splitting the path to get the file name
    file_name = svg_path.split('/')[-1]
    if '_refined.svg' in file_name:
        # Following the original naming convention
        glyph_name = file_name.replace('_refined.svg', '')
    else:
        # Backup logic to parse the .svg name as is
        glyph_name = file_name.replace('.svg', '')
    print("Parsed Glyph Name:", glyph_name)
    return glyph_name