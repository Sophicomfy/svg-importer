from svg_import_loader import load_svg_files_from_folder
from svg_import_parser import parse_glyph_name
from svg_import_converter import convert_svg_to_glyphs_layer
from svg_import_distributor import distribute_layer_to_glyph

def batch_process_svgs(folder_path):
    svg_files = load_svg_files_from_folder(folder_path)  # Step 1: Load SVG Files
    for svg_file in svg_files:
        # Step 2: Process Each SVG File Sequentially
        glyph_name = parse_glyph_name(svg_file)  # Extract glyph name from file name
        layer = convert_svg_to_glyphs_layer(svg_file)  # Convert SVG file to Glyphs layer
        if layer:
            distribute_layer_to_glyph(glyph_name, layer)  # Distribute the layer to the correct glyph
            Glyphs.font.save()  # Save the font to apply changes
        else:
            print(f"Conversion failed for {svg_file}. Skipping...")