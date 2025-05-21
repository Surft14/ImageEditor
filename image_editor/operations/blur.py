from PIL import  Image, ImageFilter
from image_editor.core import ImageEditor




class Blur(ImageEditor): #Размытие
    def apply(self, img: Image.Image) -> Image.Image:
        img = img.filter(ImageFilter.GaussianBlur(radius=self.radial))
        return img