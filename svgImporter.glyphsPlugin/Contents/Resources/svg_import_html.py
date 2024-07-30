import os
import sys
from html.parser import HTMLParser
from config import EXTRACTION_LIMIT

def log(message):
    sys.stdout.write(f"[svg_import_html] {message}\n")
    sys.stdout.flush()

def svg_import_load_html(html_file_path):
    log(f"Loading HTML file: {html_file_path}")
    temp_dir = os.path.join(os.path.dirname(html_file_path), "extracted_svgs")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    svg_import_extract_svg_files(html_content, temp_dir)
    return temp_dir

def svg_import_extract_svg_files(html_content, temp_dir):
    svgs = extract_svgs_from_html(html_content)
    log(f"Found {len(svgs)} SVGs in HTML file.")
    
    for i, svg in enumerate(svgs[:EXTRACTION_LIMIT]):  # Use the extraction limit from config.py
        svg_file_path = os.path.join(temp_dir, f"extracted_svg_{i+1}.svg")
        with open(svg_file_path, 'w', encoding='utf-8') as svg_file:
            svg_file.write(svg)
        log(f"Extracted SVG to {svg_file_path}")

def extract_svgs_from_html(html_content):
    in_svg = False
    svg_content = ""
    svgs = []

    def handle_starttag(tag, attrs):
        nonlocal in_svg, svg_content
        if tag == 'svg':
            in_svg = True
            svg_content = "<svg"
            for attr in attrs:
                svg_content += f" {attr[0]}='{attr[1]}'"
            svg_content += ">"

    def handle_endtag(tag):
        nonlocal in_svg, svg_content, svgs
        if tag == 'svg' and in_svg:
            svg_content += "</svg>"
            svgs.append(svg_content)
            in_svg = False

    def handle_data(data):
        nonlocal svg_content
        if in_svg:
            svg_content += data

    def handle_startendtag(tag, attrs):
        nonlocal svg_content
        if in_svg:
            svg_content += f"<{tag}"
            for attr in attrs:
                svg_content += f" {attr[0]}='{attr[1]}'"
            svg_content += "/>"

    parser = HTMLParser()
    parser.handle_starttag = handle_starttag
    parser.handle_endtag = handle_endtag
    parser.handle_data = handle_data
    parser.handle_startendtag = handle_startendtag

    parser.feed(html_content)
    return svgs