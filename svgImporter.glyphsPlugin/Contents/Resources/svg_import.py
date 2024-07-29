import sys
from GlyphsApp import Glyphs
from svg_import_distributor import distribute_data
from svg_import_single import svg_import_single
from svg_import_batch import svg_import_batch_load_directory, svg_import_batch_process
from svg_import_parser import parse_name_mappings, parse_glyph_name, parse_layer_name

def log(message):
    sys.stdout.write(f"[svg_import] {message}\n")
    sys.stdout.flush()

def selective_import(file_path):
    svg_file_path = svg_import_single(file_path)
    glyph_name = parse_glyph_name(svg_file_path)
    layer_name = parse_layer_name(svg_file_path)
    distribute_data(svg_file_path, glyph_name, layer_name)

def batch_import(folder_path):
    svg_files_paths = svg_import_batch_load_directory(folder_path)
    for svg_file_path in svg_import_batch_process(svg_files_paths):
        glyph_name = parse_glyph_name(svg_file_path)
        layer_name = parse_layer_name(svg_file_path)
        distribute_data(svg_file_path, glyph_name, layer_name)