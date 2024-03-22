import unittest
from src.main.lab import (
    String_concatination,String_formatting,String_slicing,To_Upper_case
)

class Testcase_for_strings(unittest.TestCase):
    def test_Concatination(self):
        result=String_concatination("Hello","World")
        self.assertEqual(result,"Hello World")
    def test_format(self):
        result=String_formatting("Shiva",23)
        self.assertEqual(result,"My name is Shiva and my age is 23")
    def test_slice(self):
        result=String_slicing("waterbottle",3,5)
        self.assertEqual(result,"er")
    def test_upper(self):
        result=To_Upper_case("apple")
        self.assertEqual(result,"APPLE")

if __name__ == '__main__':
    unittest.main()                    