# svg_import_parser.py
import xml.etree.ElementTree as ET

def parse_svg(svg_path):
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        paths = root.findall('.//{http://www.w3.org/2000/svg}path')
        path_data = [path.attrib['d'] for path in paths if 'd' in path.attrib]
        
        # Extract glyph name and character index from the filename
        filename = svg_path.split('/')[-1]
        glyph_name = filename.replace('_refined.svg', '')
        char_index = filename.split('_')[1]  # Assuming the naming convention holds

        return {'glyph_name': glyph_name, 'char_index': char_index, 'paths': path_data}
    except ET.ParseError:
        print(f"Error parsing SVG file: {svg_path}")
        return None
