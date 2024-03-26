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
            nodes.append(f"({x},{y},l)")
            i += 3
        elif command == 'C':
            cp1 = f"({round(float(commands[i+1]) * path_scale)},{round(float(commands[i+2]) * path_scale)},o)"
            cp2 = f"({round(float(commands[i+3]) * path_scale)},{round(float(commands[i+4]) * path_scale)},o)"
            end = f"({round(float(commands[i+5]) * path_scale)},{round(float(commands[i+6]) * path_scale)},c)" 
            nodes.extend([cp1, cp2, end])
            i += 7
    nodes_str = ', '.join(nodes)

    print("Converted Paths", nodes_str)
    return nodes_str

def construct_glyphs_shapes(parsed_data):
    shapes = "shapes = (\n"
    position = 0  # Initialize shape position

    for glyph_data in parsed_data:
        svg_paths = glyph_data['paths']
        for path in svg_paths:
            nodes_str = convert_svg_path_to_glyphs_nodes(path)
            # Determine if the shape is closed or open
            # This is a simplified condition; adjust according to actual logic needed
            shapeType = "closed = 1" if nodes_str.startswith("(") and nodes_str.endswith("c)") else "open = 0"
            
            # Append the formatted shape data to the shapes string
            shapes += "{\n"
            shapes += f"{shapeType}\n"  # Add shapeType
            shapes += "nodes = (\n"  # Start nodes definition
            shapes += nodes_str + "\n"  # Add nodes
            shapes += ");\n"  # Close nodes definition
            shapes += "}\n"  # Close shape definition
            position += 1  # Increment position for the next shape

    shapes += ");"  # Close the shapes collectio
    
    print("Glyphs Shapes:")
    print(shapes)
    return shapes

