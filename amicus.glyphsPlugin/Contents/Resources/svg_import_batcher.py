"""""
Code: `svg_import_batcher.py`
Goal: When running the batch import, batch the data from the loader to optimise the batch import process.
 - when loading `.svg` files from a directory (aka running "Batch Import")
 - pass the data to process {`svg_import_parser.py`, `svg_import_converter.py`, `svg_import_distributor.py`) only one `.svg` file 
 - when processed:
   - save the glyphs file
   - clean temporary stored data
   - continue to the next `.svg` file
   - print: "file name" has been processed
"""""