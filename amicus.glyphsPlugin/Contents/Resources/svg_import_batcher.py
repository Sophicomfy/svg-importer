# Code: `svg_import_batcher.py`
# Goal: When running the batch import, batch the data from the loader to optimise the batch import process.
#  - when loading `.svg` files from a directory (aka running "Batch Import")
#  - pass the data to process {`svg_import_parser.py`, `svg_import_converter.py`, `svg_import_distributor.py`) only one `.svg` file 
#  - when processed:
#     - save the glyphs file
#     - clean temporary stored data
#     - continue to the next `.svg` file
#     - print: "file name" that has been processed in batch
# - continue the loop through all the loaded files
# - end loop print: information about done

from svg_import_loader import SVGImportLoader
from svg_import_parser import parse_svg
# Assume these modules are implemented
# from svg_import_converter import convert_svg_data_to_glyphs_format
# from svg_import_distributor import distribute_glyph_data

def batch_process_svgs(folder_path):
    loader = SVGImportLoader()
    svg_files = loader.load_svg_files_from_folder(folder_path)
    
    if not svg_files:
        print("No refined SVG files to process.")
        return

    for file_path in svg_files:
        print(f"Processing: {file_path}")
        parsed_data = parse_svg(file_path, print_parsed_data=True)  # True to print parsed data for validation
        # Further processing with converter and distributor modules
        # converted_data = convert_svg_data_to_glyphs_format(parsed_data)
        # distribute_glyph_data(converted_data)

        print(f"Successfully processed and saved: {file_path.split('/')[-1]}")
    
    print("Batch import process completed.")
