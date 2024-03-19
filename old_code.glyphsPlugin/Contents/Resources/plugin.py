# encoding: utf-8

###########################################################################################################
#
#
#   General Plugin
#
#   Read the docs:
#   https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

# Assembling the code imports
from ui_main import showAmicusWindow

class AmicusSVGImporter(GeneralPlugin):

    @objc.python_method
    def settings(self):
        self.name = Glyphs.localize({
            'en': 'Amicus',
            'de': 'Amicus',
            'fr': 'Amicus',
            'es': 'Amicus',
            'pt': 'Amicus',
        })

    @objc.python_method
    def start(self):
        newMenuItem = NSMenuItem(self.name, self.showWindow_)
        Glyphs.menu[EDIT_MENU].append(newMenuItem)

# Assembling code calling functions
    def showWindow_(self, sender):
        showAmicusWindow()


    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
