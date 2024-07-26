import sys
from GlyphsApp import Glyphs
from svg_import_distributor import distribute_data
from svg_import_converter import convert_svg_to_glyphs_layer
from svg_import_parser import parse_glyph_name, parse_name_mappings
from svg_import_loader import SVGImportLoader
from svg_import_batcher import batch_process_svgs


def log(message):
    sys.stdout.write(f"[svg_import] {message}\n")
    sys.stdout.flush()

def selective_import_svg(file_path, folder_path):
    loader = SVGImportLoader()
    raw_mappings = loader.load_name_mappings(folder_path)
    name_mappings = parse_name_mappings(raw_mappings)
    distribute_data(file_path, name_mappings)

def batch_import_svgs(folder_path):
    batch_process_svgs(folder_path)