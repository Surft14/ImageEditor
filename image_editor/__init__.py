# ImageEditor/__init__.py

__version__ = "1.0.0"

__all__ = [
    "ImageIO",
    "Pipline",
    "ImageEditor",
    "Blur",
    "Brightness",
    "Color",
    "Contrast",
    "Sharpness"
]


import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

from operations.color import Color
from operations.blur import Blur
from operations.contrast import Contrast
from operations.sharpness import Sharpness
from operations.brightness import Brightness
from image_editor.io import ImageIO
from core import ImageEditor
from pipeline import Pipline

def load(path: str):
    return ImageIO.open(path)

def save(img, path: str) -> bool:
    return ImageIO.save(path, img)