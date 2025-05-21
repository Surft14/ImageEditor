from PIL import  Image, ImageEnhance
from image_editors.core import ImageEditor


class Color(ImageEditor):

    def apply(self, img: Image.Image) -> Image.Image: #Нассыщенность
        img = ImageEnhance.Color(img).enhance(factor=self.radial)
        return img