from PIL import  Image, ImageEnhance
from image_editor.core import ImageEditor


class Sharpness(ImageEditor):

    def apply(self, img: Image.Image) -> Image.Image:
        img = ImageEnhance.Sharpness(img).enhance(factor=self.radial)
        return img