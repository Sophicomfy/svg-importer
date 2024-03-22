from GlyphsApp import GSPath, GSNode, GSOFFCURVE, GSCURVE, GSLINE

def svg_command_to_glyphs_node(command, params):
    """
    Convert an SVG command with its parameters to a list of Glyphs nodes.
    """
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

def parse_svg_path(svg_path):
    nodes = []
    # Split the path string into command tokens. This is a simplified parser and may need adjustments for complex paths.
    tokens = svg_path.replace('-', ' -').split()
    i = 0

    while i < len(tokens):
        command = tokens[i]
        params = []

        if command in ['M', 'L']:
            params = [float(tokens[i + 1]), float(tokens[i + 2])]
            i += 3
        elif command == 'C':
            params = [float(tokens[i + 1]), float(tokens[i + 2]), float(tokens[i + 3]), float(tokens[i + 4]), float(tokens[i + 5]), float(tokens[i + 6])]
            i += 7

        nodes.extend(svg_command_to_glyphs_node(command, params))

    return nodes

def convert_svg_path_to_glyphs_nodes(parsed_data):
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