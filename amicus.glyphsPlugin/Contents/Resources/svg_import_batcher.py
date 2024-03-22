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
from svg_import_converter import convert_svg_path_to_glyphs_nodes
# Assume these modules are implemented
# from svg_import_distributor import distribute_glyph_data

def batch_process_svgs(folder_path):
    svg_files = SVGImportLoader().load_svg_files_from_folder(folder_path)
    
    if not svg_files:
        print("No refined SVG files to process.")
        return

    for file_path in svg_files:
        print(f"Processing: {file_path}")
        parsed_data = parse_svg(file_path, print_parsed_data=True)
        if parsed_data:
            converted_data = convert_svg_path_to_glyphs_nodes(parsed_data)
            # Assuming distribute_glyph_data is implemented and available
            # distribute_glyph_data(converted_data)
            print(f"Successfully processed: {file_path.split('/')[-1]}")
        else:
            print(f"Failed to parse: {file_path}")

    print("Batch import process completed.")