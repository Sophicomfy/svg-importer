import os
import sys
from bs4 import BeautifulSoup

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
    soup = BeautifulSoup(html_content, 'html.parser')
    svgs = soup.find_all('svg')
    log(f"Found {len(svgs)} SVGs in HTML file.")
    
    for i, svg in enumerate(svgs[:52]):  # Only extract the first 52 SVGs
        svg_file_path = os.path.join(temp_dir, f"extracted_svg_{i+1}.svg")
        with open(svg_file_path, 'w', encoding='utf-8') as svg_file:
            svg_file.write(str(svg))
        log(f"Extracted SVG to {svg_file_path}")
