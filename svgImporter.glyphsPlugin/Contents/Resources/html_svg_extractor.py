import os
import html.parser

class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.svgs = []
        self.recording = False
        self.current_svg = []

    def handle_starttag(self, tag, attrs):
        if tag == 'svg':
            self.recording = True
            self.current_svg = ['<svg']

            for attr, value in attrs:
                self.current_svg.append(f' {attr}="{value}"')
            self.current_svg.append('>')

    def handle_endtag(self, tag):
        if tag == 'svg' and self.recording:
            self.current_svg.append('</svg>')
            self.svgs.append(''.join(self.current_svg))
            self.recording = False
            self.current_svg = []

    def handle_data(self, data):
        if self.recording:
            self.current_svg.append(data)

    def handle_startendtag(self, tag, attrs):
        if tag == 'svg':
            self.handle_starttag(tag, attrs)
            self.handle_endtag(tag)

class HTMLSVGExtractor:
    def __init__(self, html_file_path, output_dir):
        self.html_file_path = html_file_path
        self.output_dir = output_dir

    def log(self, message):
        print(f"[HTMLSVGExtractor] {message}")

    def extract_svgs(self, limit=52):
        self.log(f"Reading HTML file: {self.html_file_path}")
        with open(self.html_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        parser = MyHTMLParser()
        parser.feed(content)

        svgs = parser.svgs
        self.log(f"Found {len(svgs)} SVGs in the HTML file")

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for i, svg in enumerate(svgs[:limit]):
            svg_file_path = os.path.join(self.output_dir, f"svg_{i + 1}.svg")
            with open(svg_file_path, 'w', encoding='utf-8') as svg_file:
                svg_file.write(svg)
            self.log(f"Saved SVG {i + 1} to {svg_file_path}")

        self.log(f"Extracted and saved {len(svgs[:limit])} SVGs to {self.output_dir}")

# Example usage
if __name__ == "__main__":
    # Set output directory to a writable location, such as the current working directory
    output_dir = os.path.join(os.getcwd(), 'svg_output')
    extractor = HTMLSVGExtractor('/Users/flp/Desktop/lttr_testing_20_samples/dvf_fine_tuned_on_lttr_24_800_results_20/0000/svgs_merge/800_28035.ckpt_syn_merge_0.html', output_dir)
    extractor.extract_svgs()
