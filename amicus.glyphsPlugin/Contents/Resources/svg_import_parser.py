'''
svg_import_parser.py

For `Selective Import`, bind the parsing data method and print the parsed data.
- refactor the code of involved files
- keep parser logic in `svg_import_parser.py` so that it handles only parsing regardless of selective or batch import, as `svg_import_batcher.py` always provides only one file at the batch.
- keep main logic in `svg_import.py`


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

def parse_single_svg(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        paths = [path.attrib['d'] for path in root.findall('.//{http://www.w3.org/2000/svg}path')]
        glyph_name = file_path.split('/')[-1].replace('_refined.svg', '')
        print(f"Parsed data for {glyph_name}: {paths}")
        return {'glyph_name': glyph_name, 'paths': paths}
    except Exception as e:
        print(f"Error parsing SVG file {file_path}: {e}")
        return None

'''