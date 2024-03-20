# svg_import_parser.py
import xml.etree.ElementTree as ET

def parse_svg(svg_path, print_parsed_data=False):
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        paths = [path.attrib['d'] for path in root.findall('.//{http://www.w3.org/2000/svg}path') if 'd' in path.attrib]
        
        glyph_name = svg_path.split('/')[-1].replace('_refined.svg', '')
        
        if print_parsed_data:
            print(f"Parsed data for {glyph_name}: {paths}")
            
        return {'glyph_name': glyph_name, 'paths': paths}
    except Exception as e:
        print(f"Error parsing SVG file {svg_path}: {e}")
        return None