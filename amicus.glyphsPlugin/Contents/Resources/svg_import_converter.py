from GlyphsApp import GSNode, GSLINE, GSCURVE, GSOFFCURVE

NODE_TYPES = {
    'M': 'LINE',  # Moveto maps to a line node in Glyphs
    'L': 'LINE',  # Lineto maps to a line node in Glyphs
    'C': 'CURVE',  # Curveto requires offcurve and a curve node in Glyphs
}


def convert_svg_command_to_glyphs_node_type(command):
    return NODE_TYPES.get(command, 'o')

def convert_svg_path_to_glyphs_nodes(svg_path):
    nodes = []
    commands = svg_path.split()
    path_scale = 100
    i = 0

    while i < len(commands):
        command = commands[i]
        if command in ['M', 'L']:
            x, y = round(float(commands[i+1]) * path_scale), round(float(commands[i+2]) * path_scale)
            nodes.append(f"({x},{y},l)")  # Using 'l' for line nodes
            i += 3
        elif command == 'C':
            cp1 = f"({round(float(commands[i+1]) * path_scale)},{round(float(commands[i+2]) * path_scale)},o)"
            cp2 = f"({round(float(commands[i+3]) * path_scale)},{round(float(commands[i+4]) * path_scale)},o)"
            end = f"({round(float(commands[i+5]) * path_scale)},{round(float(commands[i+6]) * path_scale)},c)" 
            nodes.extend([cp1, cp2, end])
            i += 7
    print(nodes)
    return nodes

def construct_glyphs_data_structure(parsed_data):
    if not isinstance(parsed_data, list):
        parsed_data = [parsed_data]

    glyphs_data = []

    for glyph_data in parsed_data:
        glyph_name = glyph_data['glyph_name']
        svg_paths = glyph_data['paths']
        glyphs_nodes = []

        for path in svg_paths:
            nodes = convert_svg_path_to_glyphs_nodes(path)
            glyphs_nodes.append({"closed": 1, "nodes": nodes})

        construct_glyph = {
            "glyphname": glyph_name,
            "layers": [{"shapes": [{"closed": 1, "nodes": glyphs_nodes}]}]
        }
        glyphs_data.append(construct_glyph)

    print("Converted Glyphs Data:", glyphs_data)
    return glyphs_data