from core import ImageEditor
from typing import List
from PIL import Image

class Pipeline(ImageEditor):

    steps: List[ImageEditor] = None

    def __init__(self, steps: List[ImageEditor] = None):
        self.steps: List[ImageEditor] = steps or None

    def add(self, editor: ImageEditor):
        self.steps.append(editor)
        return self

    def apply(self, img: Image.Image) -> Image.Image:
        for step in self.steps:
            img = step.apply(img)
        return img