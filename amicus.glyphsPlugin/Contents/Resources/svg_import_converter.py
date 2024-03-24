from GlyphsApp import GSNode, GSLINE, GSCURVE, GSOFFCURVE

NODE_TYPES = {
    'M': 'LINE',  # Moveto maps to a line node in Glyphs
    'L': 'LINE',  # Lineto maps to a line node in Glyphs
    'C': 'CURVE',  # Curveto requires offcurve and a curve node in Glyphs
}

def convert_svg_command_to_glyphs_node_type(command):
    return NODE_TYPES.get(command, 'OFFCURVE')

def convert_svg_path_to_glyphs_nodes(svg_path):
    nodes = []
    commands = svg_path.split()
    i = 0

    while i < len(commands):
        command = commands[i]
        node_type = convert_svg_command_to_glyphs_node_type(command)        
        if command in ['M', 'L']:
            x, y = float(commands[i+1]), float(commands[i+2])
            nodes.append((x, y, 'l'))  # Using 'l' for line nodes
            i += 3        
        elif command == 'C':
            # Control points
            cp1 = (float(commands[i+1]), float(commands[i+2]), 'o')
            cp2 = (float(commands[i+3]), float(commands[i+4]), 'o')
            # End point
            end = (float(commands[i+5]), float(commands[i+6]), 'c')  # Using 'c' for curve nodes
            nodes.extend([cp1, cp2, end])
            i += 7
        
    return nodes

def construct_glyphs_data_structure(parsed_data):
    glyphs_data = []

    for glyph_data in parsed_data:
        glyph_name = glyph_data['glyph_name']
        paths_data = glyph_data['paths']
        shapes = []

        for path_data in paths_data:
            nodes = convert_svg_path_to_glyphs_nodes(path_data)
            shape = {"closed": 1, "nodes": nodes}
            shapes.append(shape)

        glyph_structure = {
            "glyph_name": glyph_name,
            "layers": [{"shapes": shapes}]
        }

        glyphs_data.append(glyph_structure)

    print("Glyphs data:", glyphs_data)
    return glyphs_data


## Testing results
- [x] code updated, plugin reinstalled, glyphs restarted
- [x] clicked `Amicus` →  open: `Amicus UI Window`
- [x] clicked on `Batch Import`→ open:  `folder dialogue`
- [x] selected folder and clicked "open" → print: parsed data as expected
- [x] clicked on `Selective Import`→ open:  `file dialogue`
- [x] selected file and clicked "open" → print: parsed data as expected

## Next step
Goal: Convert the data with `svg_import_converter.py`
Tasks:
- [ ] Use browser extension to search for how to "convert `.svg` paths into Glyphs paths"

**Do exactly what is requested!**