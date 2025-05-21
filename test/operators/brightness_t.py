import unittest
from PIL import Image, ImageChops

from image_editors.operations.brightness import Brightness


class TestBrightness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.img = Image.open("../beach.jpg")

    def test_brightness_one_factor(self):
        brig = Brightness(radial=1)
        res = brig.apply(self.img)
        diff = ImageChops.difference(res, self.img)
        bbox = diff.getbbox()
        self.assertIsNone(bbox, "Изображение изменилось при factor = 1")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)

    def test_brightness_two_factor(self):
        brig = Brightness(radial=2)
        res = brig.apply(self.img)
        diff = ImageChops.difference(res, self.img)
        bbox = diff.getbbox()
        self.assertIsNotNone(bbox, "Изображение не изменилось при factor = 2")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)


if __name__ == '__main__':
    unittest.main()