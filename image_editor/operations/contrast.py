from PIL import  Image, ImageEnhance
from image_editor.core import ImageEditor

class Contrast(ImageEditor):

    def apply(self, img: Image.Image) -> Image.Image:# контрастность
        img = ImageEnhance.Contrast(img).enhance(factor=self.radial)
        return img