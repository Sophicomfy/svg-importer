Code `svg_import_distributor.py`
Goal: Distribute converted data into respective glyph within the Glyphs file.
- For the converted data item
    - Check whether glyph with respective name exist
        - if yes: create new layer within the glyph and draw the paths from converted data
        - if not: create glyph with respective glyph name and draw the paths from converted data within that glyph
    - Save the file


The expected glyph data format:
```
{
glyphname = A;  # converted name here
layers = (
{
layerId = m01;
shapes = (      # converted nodes data here
{
closed = 1;
nodes = (
(433,72,o),
(529,168,o),
(529,287,cs),
(529,405,o),
(433,501,o),
(315,501,cs),
(196,501,o),
(100,405,o),
(100,287,cs),
(100,168,o),
(196,72,o),
(315,72,cs)
);
}
);
width = 600;
}
);
unicode = 65;
}
```