import unittest
from PIL import Image, ImageChops
from image_editors.operations.color import Color

class TestColor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.img = Image.open("../beach.jpg")

    def test_color_one_factor(self):
        color = Color(radial=1)
        res = color.apply(self.img)
        diff = ImageChops.difference(self.img, res)
        bbox = diff.getbbox()
        self.assertIsNone(bbox, "изображение отличаеться при factor = 1")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)

    def test_color_two_factor(self):
        color = Color(radial=2)
        res = color.apply(self.img)
        diff = ImageChops.difference(res, self.img)
        bbox = diff.getbbox()
        self.assertIsNotNone(bbox, "изображение не изменилось при factor = 2")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)

if __name__ == '__main__':
    unittest.main()