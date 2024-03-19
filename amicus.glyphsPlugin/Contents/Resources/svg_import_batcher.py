"""""
Code: `svg_import_batcher.py`
Goal: When running the batch import, batch the data from the loader to optimise the batch import process.
 - when loading `.svg` files from a directory (aka running "Batch Import")
 - pass the data to process {`svg_import_parser.py`, `svg_import_converter.py`, `svg_import_distributor.py`) only one `.svg` file 
 - when processed:
    - save the glyphs file
    - clean temporary stored data
    - continue to the next `.svg` file
    - print: "file name" that has been processed in batch
- continue the loop through all the loaded files
- end loop print: information about done
"""""

from svg_import_parser import parse_svg
from svg_import_converter import convert_svg_data_to_glyphs_format
from svg_import_distributor import distribute_to_glyphs
from GlyphsApp import Glyphs

class SVGBatcher:
    def __init__(self, svg_files):
        self.svg_files = svg_files

    def process_batch(self):
        for file_path in self.svg_files:
            svg_data = parse_svg(file_path)
            if svg_data:
                converted_data = convert_svg_data_to_glyphs_format(svg_data)
                distribute_to_glyphs(converted_data)
                
                # Save Glyphs file after each SVG processing
                Glyphs.document.save()
                
                print(f"Processed in batch: {file_path.split('/')[-1]}")
                
                # Cleanup or reset temporary data if needed
                # This step depends on how your parsing, conversion, and distribution functions are implemented
                # For example, you might need to reset some class attributes or clear lists/dictionaries

        print("Batch processing done. All SVG files have been processed.")