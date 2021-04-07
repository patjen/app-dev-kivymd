from kivymd.color_definitions import colors
from kivy.utils import get_color_from_hex

def get_color(self, color, hue):
    return get_color_from_hex(colors[color][hue])