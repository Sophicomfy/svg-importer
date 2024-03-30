import GlyphsApp
from svg_import_loader import SVGImportLoader
from svg_import_converter import convert_svg_to_glyphs_layer
from svg_import_parser import parse_glyph_name

def batch_process_svgs(folder_path):
    loader = SVGImportLoader()
    svg_files = loader.load_svg_files_from_folder(folder_path)
    for svg_file in svg_files:
        layer = convert_svg_to_glyphs_path(svg_file)
        glyph_name = parse_glyph_name(svg_file)  # Using the existing parsing logic

        glyph = Glyphs.font.glyphs[glyph_name]
        if not glyph:
            glyph = GlyphsApp.GSGlyph(glyph_name)
            glyph.name = glyph_name
            Glyphs.font.glyphs.append(glyph)
        
        iteration_number = len(glyph.layers)
        layer.name = f"imported_svg_{iteration_number}"
        glyph.layers.append(layer)
        print(f"SVG from {svg_file} imported into glyph '{glyph_name}' with layer named '{layer.name}'.")