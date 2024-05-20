from GlyphsApp import GSLayer
import objc
from Foundation import NSURL, NSClassFromString
GSSVGtoPath = NSClassFromString("GSSVGtoPath")


def convert_svg_to_glyphs_layer(svg_file_path):
    layer = GSLayer()
    svg_to_path = GSSVGtoPath.alloc().init()
    url = NSURL.fileURLWithPath_(svg_file_path)

    bounds = None
    error = None
    
    success = svg_to_path.readFile_toLayer_bounds_error_(url, layer, bounds, error)
    if success:
        print(f"SVG converted successfully for {svg_file_path}")
        return layer
    else:
        if error:
            print(f"Error during SVG conversion for {svg_file_path}: {error.localizedDescription()}")
        else:
            print(f"Error during SVG conversion for {svg_file_path}, but no error details were provided.")
        return None