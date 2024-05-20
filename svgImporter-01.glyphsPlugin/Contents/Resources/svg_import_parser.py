import os

def parse_glyph_name(svg_file_path):
    file_name = os.path.basename(svg_file_path)
    parts = file_name.split('_')
    if len(parts) >= 3 and parts[1].isdigit() and parts[2].isdigit():
        glyph_name = '_'.join(parts[:2])
        return glyph_name
    else:
        return os.path.splitext(file_name)[0]

def parse_layer_name(svg_file_path):
    file_name = os.path.basename(svg_file_path)
    parts = file_name.split('_')
    if len(parts) >= 3 and parts[1].isdigit() and parts[2].isdigit():
        layer_name = parts[2]
        return layer_name
    else:
        return os.path.splitext(file_name)[0]
