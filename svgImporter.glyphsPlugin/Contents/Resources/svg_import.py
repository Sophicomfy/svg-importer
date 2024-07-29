import sys
from GlyphsApp import Glyphs
from svg_import_single import SVGImportLoader
from svg_import_batch import batch_process_svgs
from svg_import_parser import parse_name_mappings
from svg_import_distributor import distribute_data

def log(message):
    sys.stdout.write(f"[svg_import] {message}\n")
    sys.stdout.flush()

def selective_import_svg(file_path):
    loader = SVGImportLoader()
    raw_mappings = loader.load_name_mappings(file_path)
    name_mappings = parse_name_mappings(raw_mappings)
    distribute_data(file_path)

def batch_import_svgs(folder_path):
    batch_process_svgs(folder_path)
