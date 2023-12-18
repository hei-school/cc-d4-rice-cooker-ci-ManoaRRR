import unittest
from riceCoocker import RiceCooker

class TestRiceCooker(unittest.TestCase):
    def setUp(self):
        self.rice_cooker = RiceCooker()

    def test_set_rice_type(self):
        self.rice_cooker.set_rice_type('riz blanc')
        self.assertEqual(self.rice_cooker.rice_type, 'riz blanc')

    def test_set_water_level(self):
        self.rice_cooker.set_water_level(50)
        self.assertEqual(self.rice_cooker.water_level, 50)

    def test_set_invalid_water_level(self):
        with self.assertRaises(ValueError):
            self.rice_cooker.set_water_level(120)

    def test_set_cooking_time(self):
        self.rice_cooker.set_cooking_time(0.5)
        self.assertEqual(self.rice_cooker.cooking_time, 0.5)

    def test_set_invalid_cooking_time(self):
        with self.assertRaises(ValueError):
            self.rice_cooker.set_cooking_time(70)

    # def test_start_cooking(self):
    #     self.rice_cooker.set_rice_type('riz blanc')
    #     self.rice_cooker.set_water_level(50)
    #     self.rice_cooker.set_cooking_time(0.1)
    #     self.rice_cooker.start_cooking()
    #     self.assertTrue(self.rice_cooker.is_cooking)

    def test_stop_cooking(self):
        self.rice_cooker.is_cooking = True
        self.rice_cooker.stop_cooking()
        self.assertFalse(self.rice_cooker.is_cooking)

    

    def test_check_cooking_status_not_cooking(self):
        expected_status = "État du cuiseur à riz - Type de riz: , Niveau d'eau: 0%, Cuisson en cours: Non"
        self.assertEqual(self.rice_cooker.check_cooking_status(), expected_status)

if __name__ == '__main__':
    unittest.main()
