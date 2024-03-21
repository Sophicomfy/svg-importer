from GlyphsApp import GSPath, GSNode, GSOFFCURVE, GSCURVE, GSLINE
import re

def convert_svg_paths_to_glyphs(svg_data):
    converted_paths = []
    for path_data in svg_data.get('paths', []):
        gs_path = GSPath()
        path_commands = re.findall(r'[MLC][^MLC]*', path_data)  # Split path data into commands

        for command in path_commands:
            cmd_type = command[0]
            points = [float(coord) for coord in command[1:].strip().split()]
            points_iter = iter(points)
            point_pairs = list(zip(points_iter, points_iter))

            if cmd_type == 'M':  # MoveTo command
                # MoveTo is handled implicitly by starting a new GSPath, as GSPath always starts with a moveTo
                pass
            elif cmd_type == 'C':  # Cubic Bézier Curve command
                for i, (x, y) in enumerate(point_pairs):
                    node_type = GSOFFCURVE if i < 2 else GSCURVE  # First two points are off-curve, last is on-curve
                    gs_node = GSNode((x, y), node_type)
                    gs_path.nodes.append(gs_node)

        gs_path.closed = True if path_data.endswith('Z') else False  # Check if path should be closed
        converted_paths.append(gs_path)

    print(f"Converted {len(converted_paths)} paths for glyph: {svg_data.get('glyph_name')}")
    return converted_paths