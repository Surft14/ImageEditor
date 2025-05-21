import unittest
import os
from PIL import Image
from image_editor.io import ImageIO
from tempfile import NamedTemporaryFile


class TestImageIO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.img = ImageIO.open("beach.jpg")

    def test_open_returns_image(self):
        self.assertIsInstance(self.img, Image.Image)

    def test_save_success(self):
        with NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            tmp_path = tmp.name
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

        ok = ImageIO.save(tmp_path, self.img)
        self.assertTrue(ok, "Метод save вернул False для валидного пути")
        self.assertTrue(os.path.exists(tmp_path), "Файл не был создан")

        reopened = Image.open(tmp_path)
        self.assertEqual(reopened.size, self.img.size)
        reopened.close()

        os.remove(tmp_path)

    def test_save_failure(self):
        bad_path = "/no_such_dir/out.png"
        ok = ImageIO.save(bad_path, self.img)
        self.assertFalse(ok, "Метод save вернул True для невалидного пути")

    def test_convert_jpeg(self):
        self.assertEqual(self.img.mode, "RGB",
                         "Ожидается, что beach.jpg в режиме RGB")
        converted = ImageIO.convert(None, self.img, "jpg")
        self.assertIsInstance(converted, Image.Image, "Метод convert должен возвращать объект PIL.Image.Image")
        self.assertEqual(converted.mode, "RGB",
                         "RGB -> JPG не должно менять режим")
        self.assertEqual(converted.size, self.img.size)

    def test_convert_png(self):
        converted = ImageIO.convert(None, self.img, "png")
        self.assertIsInstance(converted, Image.Image)
        self.assertEqual(converted.mode, "RGB",
                         "RGB -> PNG не должно менять режим")
        self.assertEqual(converted.size, self.img.size)