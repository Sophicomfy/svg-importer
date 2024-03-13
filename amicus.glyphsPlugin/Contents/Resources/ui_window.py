# ui_window.py
from vanilla import Window

class AmicusWindow:
    def __init__(self):
        self.window = Window((200, 70), "Amicus")
        self.window.textBox = TextBox((10, 10, -10, -10), "Amicus is running", sizeStyle='small')
        self.window.open()
