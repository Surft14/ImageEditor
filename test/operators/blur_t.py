import unittest
from PIL import Image, ImageChops

from image_editors.operations.blur import Blur


class TestBlur(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.img = Image.open("../beach.jpg")

    def test_blur_zero_radius(self):
        blur = Blur(radial=0)
        res = blur.apply(self.img)
        diff = ImageChops.difference(self.img, res)
        bbox = diff.getbbox()
        self.assertIsNone(bbox, "Изображения отличаются при radius=0")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)

    def test_blur_positive_radius(self):
        blur = Blur(radial=5)
        res = blur.apply(self.img)
        diff = ImageChops.difference(self.img, res)
        bbox = diff.getbbox()
        self.assertIsNotNone(bbox, "Изображение не изменилось при radius>0")
        self.assertEqual(res.size, self.img.size )
        self.assertEqual(res.mode, self.img.mode )



if __name__ == '__main__':
    unittest.main()
