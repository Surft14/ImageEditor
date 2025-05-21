import unittest

from PIL import Image, ImageChops

from operators.blur import Blur
from operators.brightness import Brightness
from operators.color import Color
from operators.contrast import Contrast
from operators.sharpness import Sharpness
from image_editor.pipeline import Pipeline


class TestPipline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.img = Image.open("beach.jpg")

    def test_add_first_method(self):

        pip = Pipeline([
            Blur(radial=5),
            Brightness(radial=3),
            Color(radial=3),
            Contrast(radial=3),
            Sharpness(radial=3)
        ])

        self.assertIsNotNone(pip.steps, "Список шагов не изменился")

    def test_add_second_method(self):
        pip = (
            Pipeline()
            .add(Blur(radial=5))
            .add(Brightness(radial=3))
            .add(Color(radial=3))
            .add(Contrast(radial=3))
            .add(Sharpness(radial=3))
        )

        self.assertIsNotNone(pip.steps, "Список шагов не изменился")

    def test_apply(self):
        listEditors = [
            Blur(radial=5),
            Brightness(radial=3),
            Color(radial=3),
            Contrast(radial=3),
            Sharpness(radial=3)
        ]
        i = 0
        for step in listEditors:
            img_tmp = step.apply(self.img)
            diff = ImageChops.difference(img_tmp, self.img)
            bbox = diff.getbbox()
            self.assertIsNotNone(bbox, f"Изображение не изменилось step = {i}")
            i += 1

if __name__ == '__main__':
    unittest.main()
