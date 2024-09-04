import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_four_character(self):
        self.assertEqual(generate_soundex("FGTM"), "F235")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("BFPV"), "B000")
        
    def test_string_with_special_characters(self):
        self.assertEqual(generate_soundex("1@!Abc3"),"1120")
        
    def test_string_with_vowels(self):
        self.assertEqual(generate_soundex("Robert"),"R163")

    def test_string_with_numbers(self):
        self.assertEqual(generate_soundex("1234"),"1000")     


    def test_failure_case(self):
        self.assertNotEqual(generate_soundex("Honeyman"), "H554")

if __name__ == '__main__':
    unittest.main()
