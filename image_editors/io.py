from PIL import Image
from _io import BytesIO

class ImageIO:
    @staticmethod
    def open(path:str) -> Image.Image:
        img = Image.open(path)
        return img

    @staticmethod
    def save(path:str, img: Image.Image) -> bool:
        try:
            img.save(path)
            return True
        except:
            return False

    @staticmethod
    def convert(self, img:Image.Image, format: str) -> Image.Image:

        fmt = format.upper()
        if fmt in ("JPG", "JPEG") and img.mode != "RGB":
            img = img.convert("RGB")
        elif fmt == "PNG" and img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGBA")

        buffer = BytesIO()
        img.save(buffer, format=fmt)
        buffer.seek(0)
        return Image.open(buffer)