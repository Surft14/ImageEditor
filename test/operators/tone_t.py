import unittest

from PIL import Image, ImageChops
from image_editor.operations import Tone

class TestTone(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.img = Image.open("../beach.jpg")

    def test_tone_zero_hue(self):
        tone = Tone(hue_shift=0)
        res = tone.apply(self.img)
        diff = ImageChops.difference(self.img, res)
        bbox = diff.getbbox()
        self.assertIsNone(bbox, "Изображение изменилось при 0 градусов")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)

    def test_tone_positive_hue(self):
        tone = Tone(hue_shift=180)
        res = tone.apply(self.img)
        diff = ImageChops.difference(self.img, res)
        bbox = diff.getbbox()
        self.assertIsNotNone(bbox, "Изображение не изменилось при 180 градусов")
        self.assertEqual(res.size, self.img.size)
        self.assertEqual(res.mode, self.img.mode)



if __name__ == '__main__':
    unittest.main()