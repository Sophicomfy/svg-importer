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

def parse_name_mappings(raw_content):
    name_mappings = {}
    lines = raw_content.strip().split('\n')
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 2:
            key, value = parts[0].strip(), parts[1].strip()
            name_mappings[key] = value
        else:
            sys.stdout.write(f"Skipping invalid line in name mappings: {line}\n")
            sys.stdout.flush()
    sys.stdout.write(f"[svg_import_parser] Parsed name mappings: {name_mappings}\n")
    sys.stdout.flush()
    return name_mappings