from GlyphsApp import GSNode, GSLINE, GSCURVE, GSOFFCURVE

def convert_svg_path_to_glyphs_nodes(svg_path):
    nodes = []
    commands = svg_path.split()
    i = 0

    while i < len(commands):
        command = commands[i]
        if command in ['M', 'L']:
            x, y = float(commands[i+1]), float(commands[i+2])
            # Convert nodes to the tuple format (x, y, type)
            nodes.append((x, y, 'line'))
            i += 3
        elif command == 'C':
            cp1 = (float(commands[i+1]), float(commands[i+2]))
            cp2 = (float(commands[i+3]), float(commands[i+4]))
            end = (float(commands[i+5]), float(commands[i+6]))
            # Convert nodes to the tuple format including offcurve and curve types
            nodes.extend([
                (cp1[0], cp1[1], 'offcurve'),
                (cp2[0], cp2[1], 'offcurve'),
                (end[0], end[1], 'curve')
            ])
            i += 7
        # Handle other commands as necessary
    print("Converted nodes")
    print(nodes)
    return nodes


def construct_glyphs_data_structure(converted_data):
    if isinstance(converted_data, dict):
        converted_data = [converted_data]

    converted_data = []

    for glyph_data in converted_data:
        glyph_name = glyph_data.get('glyph_name', 'Unknown')
        svg_paths = glyph_data.get('paths', [])
        glyphs_nodes = []

        for path in svg_paths:
            nodes = convert_svg_path_to_glyphs_nodes(path)
            glyphs_nodes.append({"closed": True, "nodes": nodes})

        construct_glyph = {
            "glyphname": glyph_name,
            "layers": [{"shapes": [{"closed": 1, "nodes": glyphs_nodes}]}]
        }
        converted_data.append(construct_glyph)

    # Directly print the converted data to verify the output
    print(converted_data)
    return converted_data