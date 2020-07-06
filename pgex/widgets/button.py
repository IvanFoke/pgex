from pgex.widgets.text import Text
from pygame import *


class Button:
    def __init__(self, width, height, text, action=None, bg=(13, 162, 58), active_bg=(23, 204, 58)):
        self.width = width
        self.height = height
        self.text = text
        self.action = action
        self.bg = bg
        self.active_bg = active_bg
