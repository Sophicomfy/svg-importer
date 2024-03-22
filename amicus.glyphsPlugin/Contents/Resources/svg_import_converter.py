from GlyphsApp import GSNode, GSLINE, GSCURVE, GSOFFCURVE

def parse_svg_path(svg_path):
    # Initialize an empty list to store nodes for a single path
    nodes = []
    commands = svg_path.split()
    i = 0

    while i < len(commands):
        command = commands[i]
        if command in ['M', 'L']:
            # Handle 'move to' and 'line to' commands
            x, y = float(commands[i+1]), float(commands[i+2])
            # Add a line node to the nodes list
            nodes.append({"x": x, "y": y, "type": "line"})
            i += 3
        elif command == 'C':
            # Handle cubic Bezier curve command
            cp1 = (float(commands[i+1]), float(commands[i+2]))
            cp2 = (float(commands[i+3]), float(commands[i+4]))
            end = (float(commands[i+5]), float(commands[i+6]))
            # Add off-curve control points and the curve node to the nodes list
            nodes.extend([
                {"x": cp1[0], "y": cp1[1], "type": "offcurve"},
                {"x": cp2[0], "y": cp2[1], "type": "offcurve"},
                {"x": end[0], "y": end[1], "type": "curve"}
            ])
            i += 7
        # Handle other commands as necessary

    return nodes

def convert_svg_path_to_glyphs_nodes(parsed_data):
    if isinstance(parsed_data, dict):
        parsed_data = [parsed_data]
    
    converted_data = []

    for glyph_data in parsed_data:
        glyph_name = glyph_data.get('glyph_name', 'Unknown')
        svg_paths = glyph_data.get('paths', [])

        glyphs_nodes = []

        for path in svg_paths:
            nodes = parse_svg_path(path)
            glyphs_nodes.append({"closed": True, "nodes": nodes})

        converted_data.append({
            "glyphname": glyph_name,
            "layers": [{"shapes": glyphs_nodes}]
        })

    # Directly print the converted data to verify the output
    print(converted_data)
    return converted_data