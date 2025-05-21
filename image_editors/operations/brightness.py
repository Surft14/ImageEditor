from PIL import  Image, ImageEnhance
from image_editors.core import ImageEditor


class Brightness(ImageEditor):#Яркость

    def apply(self, img: Image.Image) -> Image.Image:
        img = ImageEnhance.Brightness(img).enhance(factor=self.radial)
        return img
