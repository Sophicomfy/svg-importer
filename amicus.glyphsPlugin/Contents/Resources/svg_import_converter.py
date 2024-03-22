from GlyphsApp import GSPath, GSNode, GSOFFCURVE, GSCURVE, GSLINE

def svg_command_to_glyphs_node(command, params):

    if command == 'M' or command == 'L':
        # 'M' and 'L' commands correspond to GSLINE nodes in Glyphs.
        return [((params[0], params[1]), 'line')]
    elif command == 'C':
        # 'C' command corresponds to a curve in Glyphs, requiring two offcurve nodes followed by a curve node.
        return [
            ((params[0], params[1]), 'offcurve'),
            ((params[2], params[3]), 'offcurve'),
            ((params[4], params[5]), 'curve')
        ]
    else:
        # Placeholder for handling additional SVG path commands.
        print(f"Warning: Unhandled SVG command '{command}'")
        return []

def convert_svg_paths(svg_path):
    nodes = []
    commands = svg_path.split()
    i = 0

    while i < len(commands):
        command = commands[i]
        if command == 'M' or command == 'L':
            # Move and line commands.
            x, y = float(commands[i+1]), float(commands[i+2])
            nodes.append({"x": x, "y": y, "type": "line"})  # GSLINE equivalent
            i += 3
        elif command == 'C':
            # Cubic Bezier curve command.
            for j in range(1, 7, 2):
                x, y = float(commands[i+j]), float(commands[i+j+1])
                node_type = "offcurve" if j < 5 else "curve"  # Last point of 'C' is a curve point
                nodes.append({"x": x, "y": y, "type": node_type})
            i += 7
        # Additional SVG commands can be added here.
    
    return nodes

def create_glyphs_data_structure(parsed_data):
    converted_data = []

    for glyph_data in parsed_data:
        glyph_name, svg_paths = glyph_data['glyph_name'], glyph_data['paths']
        all_nodes = [parse_svg_path(svg_path) for svg_path in svg_paths]

        converted_data.append({
            "glyphname": glyph_name,
            "layers": [{
                "shapes": [{
                    "closed": True,
                    "nodes": [node for sublist in all_nodes for node in sublist]  # Flatten the list of nodes
                }],
            }]
        })

    print(converted_data)
    return converted_data