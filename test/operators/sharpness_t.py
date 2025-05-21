import unittest

from PIL import Image, ImageChops
from image_editor.operations.sharpness import Sharpness


class TestSharpness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.img = Image.open("../beach.jpg")

    def test_sharpness_one_factor(self):
        sharp = Sharpness(radial=1)
        res = sharp.apply(self.img)
        diff = ImageChops.difference(self.img, res)
        bbox = diff.getbbox()
        self.assertIsNone(bbox, "Изображение изменилось при factor = 1")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)

    def test_sharpness_two_factor(self):
        sharp = Sharpness(radial=2)
        res = sharp.apply(self.img)
        diff = ImageChops.difference(self.img, res)
        bbox = diff.getbbox()
        self.assertIsNotNone(bbox, "Изображение не изменилось при factor = 2")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)



if __name__ == '__main__':
    unittest.main()