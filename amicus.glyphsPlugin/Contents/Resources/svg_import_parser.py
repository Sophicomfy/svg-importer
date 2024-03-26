import xml.etree.ElementTree as ET

def parse_glyph_name(svg_path):
    glyph_name = svg_path.split('/')[-1].replace('_refined.svg', '')
    print("Parsed Glyph Name")
    print(glyph_name)
    return glyph_name

def parse_path_data(svg_path):
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        paths = root.findall('.//{http://www.w3.org/2000/svg}path')
        path_data = [path.attrib['d'] for path in paths if 'd' in path.attrib]
        print("Extracted Path Data")
        print(path_data)
        return path_data
    except ET.ParseError as e:
        print(f"Error parsing SVG file {svg_path}: {e}")
        return None

def parse_svg(svg_path, print_parsed_data=False):
    glyph_name = parse_glyph_name(svg_path)
    path_data = parse_path_data(svg_path)

    parsed_data = {'glyph_name': glyph_name, 'paths': path_data}

    if print_parsed_data:
        print("Parsed data: ")
        print(parsed_data)

    return parsed_data