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

    def showWindow_(self, sender):
        # Simple notification to show that the plugin works
        Glyphs.showNotification('Amicus SVG Importer', 'The Amicus plugin is successfully running!')

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
