import unittest
from riceCoocker import RiceCooker
from unittest.mock import patch

class TestRiceCooker(unittest.TestCase):
    def setUp(self):
        self.rice_cooker = RiceCooker()

    def test_set_rice_type(self):
        self.rice_cooker.set_rice_type('riz basmati')
        self.assertEqual(self.rice_cooker.rice_type, 'riz basmati')

    def test_set_water_level(self):
        self.rice_cooker.set_water_level(40)
        self.assertEqual(self.rice_cooker.water_level, 40)

    def test_set_cooking_time(self):
        self.rice_cooker.set_cooking_time(15)
        self.assertEqual(self.rice_cooker.cooking_time, 15)

    def test_start_cooking_successful(self):
        self.rice_cooker.set_rice_type('riz complet')
        self.rice_cooker.set_water_level(60)
        self.rice_cooker.set_cooking_time(20)

        with unittest.mock.patch('time.sleep', return_value=None):
            self.rice_cooker.start_cooking()

        self.assertFalse(self.rice_cooker.is_cooking)

    def test_start_cooking_invalid_rice_type(self):
        with self.assertRaises(ValueError):
            self.rice_cooker.start_cooking()

    def test_start_cooking_invalid_water_level(self):
        self.rice_cooker.set_rice_type('riz blanc')
        with self.assertRaises(ValueError):
            self.rice_cooker.start_cooking()

    def test_start_cooking_invalid_cooking_time(self):
        self.rice_cooker.set_rice_type('riz complet')
        self.rice_cooker.set_water_level(70)
        with self.assertRaises(ValueError):
            self.rice_cooker.start_cooking()

    def test_stop_cooking_successful(self):
        self.rice_cooker.is_cooking = True
        self.rice_cooker.stop_cooking()
        self.assertFalse(self.rice_cooker.is_cooking)

    def test_stop_cooking_not_cooking(self):
        self.rice_cooker.is_cooking = False
        with self.assertWarns(UserWarning):
            self.rice_cooker.stop_cooking()

if __name__ == '__main__':
    unittest.main()
