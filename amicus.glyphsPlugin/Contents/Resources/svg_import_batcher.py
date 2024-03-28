from GlyphsApp import GSSVGtoPath, Glyphs
from svg_import_loader import SVGImportLoader

def batch_import_svgs(folder_path):
    loader = SVGImportLoader()
    svg_files = loader.load_svg_files_from_folder(folder_path)
    for svg_file in svg_files:
        glyph_name = determine_glyph_name_from_file(svg_file)
        glyph = Glyphs.font.glyphs[glyph_name]
        if not glyph:
            print(f"No glyph named {glyph_name} found for SVG {svg_file}. Skipping...")
            continue
        glyph.layers.append(GSSVGtoPath(svg_file))
        print(f"SVG from {svg_file} imported into glyph {glyph_name}.")
