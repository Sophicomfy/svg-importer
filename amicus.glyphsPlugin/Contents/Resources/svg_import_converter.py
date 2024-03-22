def convert_svg_path_to_glyphs_nodes(parsed_data):
    converted_data = []

    for glyph_data in parsed_data:
        glyph_name = glyph_data.get('glyph_name', 'Unknown')
        svg_paths = glyph_data.get('paths', [])
        glyphs_layers = []

        for path in svg_paths:
            glyphs_nodes = parse_svg_path(path)
            glyphs_layers.append({
                "closed": 1,  # Use 1 for true to match the desired format
                "nodes": glyphs_nodes
            })

        converted_data.append({
            "glyphname": glyph_name,
            "layers": [{"shapes": glyphs_layers}]
        })

    # Convert and print the data in the desired format for verification
    print_converted_data(converted_data)
    return converted_data

def parse_svg_path(svg_path):
    nodes = []
    commands = svg_path.split()
    i = 0

    while i < len(commands):
        command = commands[i]
        if command in ['M', 'L']:
            x, y = float(commands[i+1]), float(commands[i+2])
            nodes.append((x, y, 'l'))  # Use 'l' for line nodes
            i += 3
        elif command == 'C':
            cp1 = (float(commands[i+1]), float(commands[i+2]), 'o')
            cp2 = (float(commands[i+3]), float(commands[i+4]), 'o')
            end = (float(commands[i+5]), float(commands[i+6]), 'c')  # Use 'c' for curve endpoint
            nodes.extend([cp1, cp2, end])
            i += 7

    return nodes

def print_converted_data(converted_data):
    for data_item in converted_data:
        print(f"glyphname = {data_item['glyphname']}")
        for layer in data_item['layers']:
            for shape in layer['shapes']:
                print("closed =", shape['closed'])
                print("nodes = (")
                for node in shape['nodes']:
                    print(f"({node[0]},{node[1]},{node[2]})")
                print(");")


    print(converted_data)
    return converted_data