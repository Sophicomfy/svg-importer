# Code `svg_import_distributor.py`
# Goal: Distribute converted data into respective glyphs within the glyphs file.
# - For the converted data item
#     - Check whether glyph with respective name exist
#         - if yes: create new layer within the glyph and draw the paths from converted data
#         - if not: create glyph with respective glyph name and draw the paths from converted data within that glyph
#     - Save the file