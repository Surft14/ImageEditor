import numpy as np
import colorsys
from PIL import Image
from image_editor.core import ImageEditor


class Tone(ImageEditor):
    def __init__(self, hue_shift: float):
        self.hue_shift = hue_shift  # 0–360

    def apply(self, img: Image.Image) -> Image.Image:
        if self.hue_shift == 0:
            return img

        if img.mode != 'RGB':
            img = img.convert('RGB')

        np_img = np.array(img) / 255.0
        r, g, b = np_img[..., 0], np_img[..., 1], np_img[..., 2]
        h, s, v = np.vectorize(colorsys.rgb_to_hsv)(r, g, b)
        h = (h + self.hue_shift / 360.0) % 1.0
        r, g, b = np.vectorize(colorsys.hsv_to_rgb)(h, s, v)
        new_img = np.stack([r, g, b], axis=-1) * 255
        new_img = new_img.astype('uint8')
        return Image.fromarray(new_img)