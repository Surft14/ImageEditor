import unittest

from PIL import Image, ImageChops

from image_editors.operations.contrast import Contrast


class TestContrast(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.img = Image.open("../beach.jpg")

    def test_contrast_one_factor(self):
        con = Contrast(radial=1)
        res = con.apply(self.img)
        diff = ImageChops.difference(res, self.img)
        bbox = diff.getbbox()
        self.assertIsNone(bbox, "Изображение изменилось при factor = 1")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)

    def test_contrast_two_factor(self):
        con = Contrast(radial=2)
        res = con.apply(self.img)
        diff = ImageChops.difference(res, self.img)
        bbox = diff.getbbox()
        self.assertIsNotNone(bbox, "Изображение не изменилось при factor = 2")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)

if __name__ == '__main__':
    unittest.main()