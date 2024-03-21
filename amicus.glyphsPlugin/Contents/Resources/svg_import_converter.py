from GlyphsApp import GSPath, GSNode, GSOFFCURVE, GSCURVE, GSLINE
import re

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
            if command == 'M':
                x, y = float(commands[i+1]), float(commands[i+2])
                path_nodes.append({'type': 'line', 'position': (x, y)})
                i += 3
            elif command == 'C':
                cp1x, cp1y = float(commands[i+1]), float(commands[i+2])
                path_nodes.append({'type': 'offcurve', 'position': (cp1x, cp1y)})
                cp2x, cp2y = float(commands[i+3]), float(commands[i+4])
                path_nodes.append({'type': 'offcurve', 'position': (cp2x, cp2y)})
                ex, ey = float(commands[i+5]), float(commands[i+6])
                path_nodes.append({'type': 'curve', 'position': (ex, ey)})
                i += 7
        
        glyphs_nodes.append({'closed': True, 'nodes': path_nodes})
    
    print_forwarded_data(glyph_name, glyphs_nodes)
    
    return glyphs_nodes

def print_forwarded_data(glyph_name, glyphs_nodes):
    print(f"Forwarding the following data for {glyph_name} to svg_import_distributor.py:")
    for path_index, path in enumerate(glyphs_nodes):
        print(f"  Path {path_index + 1}: Closed: {path['closed']}, Nodes:")
        for node in path['nodes']:
            print(f"    Type: {node['type']}, Position: {node['position']}")
