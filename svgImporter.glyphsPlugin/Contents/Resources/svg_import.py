import sys
from GlyphsApp import Glyphs
from svg_import_single import svg_import_single, load_name_mappings
from svg_import_batch import svg_import_batch_load_directory, svg_import_batch_process
from svg_import_html import svg_import_load_html
from svg_import_parser import parse_name_mappings, parse_glyph_name, parse_layer_name
from svg_import_distributor import distribute_data


def log(message):
    sys.stdout.write(f"[svg_import] {message}\n")
    sys.stdout.flush()

def selective_import(file_path):
    svg_file_path = svg_import_single(file_path)
    if svg_file_path:
        glyph_name = parse_glyph_name(svg_file_path)
        layer_name = parse_layer_name(svg_file_path)
        distribute_data(svg_file_path, glyph_name, layer_name)

def batch_import(folder_path):
    svg_files_paths = svg_import_batch_load_directory(folder_path)
    for svg_file_path in svg_import_batch_process(svg_files_paths):
        glyph_name = parse_glyph_name(svg_file_path)
        layer_name = parse_layer_name(svg_file_path)
        distribute_data(svg_file_path, glyph_name, layer_name)

def html_import(html_file_path):
    temp_dir = svg_import_load_html(html_file_path)
    svg_files_paths = svg_import_batch_load_directory(temp_dir)
    for svg_file_path in svg_import_batch_process(svg_files_paths[:52]):  # Limit to first 52 SVGs
        glyph_name = parse_glyph_name(svg_file_path)
        layer_name = parse_layer_name(svg_file_path)
        distribute_data(svg_file_path, glyph_name, layer_name)
