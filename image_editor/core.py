from PIL import Image
from abc import ABC, abstractmethod

class ImageEditor(ABC):
    radial: int

    def __init__(self, *, radial:int):
        self.radial = radial

    @abstractmethod
    def apply(self, img: Image.Image) -> Image.Image:
        return img

