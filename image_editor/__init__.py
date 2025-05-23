# ImageEditor/__init__.py

__version__ = "1.1.1"

__all__ = [
    "ImageIO",
    "Pipeline",
    "ImageEditor",
    "Blur",
    "Brightness",
    "Color",
    "Contrast",
    "Sharpness",
    "Tone",
    "load",
    "save"
]


import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

from .operations.color import Color
from .operations.blur import Blur
from .operations.contrast import Contrast
from .operations.sharpness import Sharpness
from .operations.brightness import Brightness
from .operations.tone import Tone
from .io import ImageIO
from .pipeline import Pipeline
from .core import ImageEditor

def load(path: str):
    return ImageIO.open(path)

def save(img, path: str) -> bool:
    return ImageIO.save(path, img)