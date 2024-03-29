from GlyphsApp import GSLayer, GSSVGtoPath
import objc
from Foundation import NSURL

def convert_svg_to_glyphs_layer(svg_file_path):
    layer = GSLayer()
    svg_to_path = GSSVGtoPath.alloc().init()
    url = NSURL.fileURLWithPath_(svg_file_path)
    
    success = svg_to_path.readFile_toLayer_error_(url, layer, None)
    if success:
        print(layer)
        return layer
    else:
        print("Error during SVG conversion.")
        return None