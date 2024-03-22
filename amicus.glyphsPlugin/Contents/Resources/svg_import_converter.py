from GlyphsApp import GSPath, GSNode, GSOFFCURVE, GSCURVE, GSLINE

def convert_svg_path_to_glyphs_nodes(parsed_data):
    glyph_name = parsed_data['glyph_name']
    svg_paths = parsed_data['paths']
    glyphs_nodes = []

    for svg_path in svg_paths:
        path_nodes = parse_svg_path(svg_path)
        glyphs_nodes.append({'closed': True, 'nodes': path_nodes})
    
    print_forwarded_data(glyph_name, glyphs_nodes)
    return glyphs_nodes

def convert_svg_path_to_glyphs_nodes(parsed_data):
    glyph_name = parsed_data['glyph_name']
    svg_paths = parsed_data['paths']
    
    glyphs_nodes = []
    
    for svg_path in svg_paths:
        commands = svg_path.split()
        path_nodes = []
        i = 0

        while i < len(commands):
            command = commands[i]
            if command == 'M' or command == 'L':
                x, y = float(commands[i+1]), float(commands[i+2])
                # Correction: Ensure position is a tuple of floats
                path_nodes.append(GSNode((x, y), GSLINE))
                i += 3
            elif command == 'C':
                # Handling cubic bezier curves with OFFCURVE and CURVE nodes
                cp1x, cp1y = float(commands[i+1]), float(commands[i+2])
                cp2x, cp2y = float(commands[i+3]), float(commands[i+4])
                ex, ey = float(commands[i+5]), float(commands[i+6])
                path_nodes.extend([
                    GSNode((cp1x, cp1y), GSOFFCURVE),
                    GSNode((cp2x, cp2y), GSOFFCURVE),
                    GSNode((ex, ey), GSCURVE)
                ])
                i += 7
            else:
                print(f"Unsupported command: {command}")
                break

        glyphs_nodes.append({'closed': True, 'nodes': path_nodes})

    print_forwarded_data(glyph_name, glyphs_nodes)

    return path_nodes

def print_forwarded_data(glyph_name, glyphs_nodes):
    print(f"Forwarding the following data for {glyph_name} to svg_import_distributor.py:")
    for path_index, path in enumerate(glyphs_nodes):
        print(f"  Path {path_index + 1}: Closed: {path['closed']}, Nodes:")
        for node in path['nodes']:
            print(f"    Type: {node.type}, Position: {node.position}")

