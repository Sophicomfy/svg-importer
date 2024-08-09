import os
import csv
from GlyphsApp import Glyphs
from config import MAPPINGS_ORIG, MAPPINGS_NEW, NAME_MAPPINGS_PATH

def load_name_mappings():
    script_dir = os.path.dirname(os.path.realpath(__file__))

    mappings = {}
    try:
        with open(full_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                orig_name = row[MAPPINGS_ORIG].strip()
                new_name = row[MAPPINGS_NEW].strip()
                if orig_name and new_name:
                    mappings[orig_name] = new_name
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise

    return mappings

def rename_glyphs(font, mappings):
    for glyph in font.glyphs:
        if glyph.name in mappings:
            glyph.name = mappings[glyph.name]

def run_name_conversion():
    font = Glyphs.font
    mappings = load_name_mappings()
    rename_glyphs(font, mappings)
    font.save()

if __name__ == "__main__":
    run_name_conversion()
