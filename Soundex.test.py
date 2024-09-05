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

    def test_repeated_characters(self):
        self.assertEqual(generate_soundex("Tomm"), "T500")

    def test_name_starting_with_vowel(self):
        self.assertEqual(generate_soundex("Andrew"), "A536")

    def test_same_consonant_group(self):
        self.assertEqual(generate_soundex("Pfister"), "P236")

    def test_multiple_vowels(self):
        self.assertEqual(generate_soundex("Euler"), "E460")

    def test_only_vowels(self):
        self.assertEqual(generate_soundex("Aeio"), "A000")
    
    def test_name_with_spaces(self):
        self.assertEqual(generate_soundex("John Doe"), "J530")
    
    def test_lowercase_name(self):
        self.assertEqual(generate_soundex("smith"), "S530")

    def test_name_with_hyphens(self):
        self.assertEqual(generate_soundex("Smith-Jones"), "S532")
        
    def test_name_with_apostrophes(self):
        self.assertEqual(generate_soundex("O'Connor"), "O256")
        
    def test_mixed_case_name(self):
        self.assertEqual(generate_soundex("McDonald"), "M235")
        
    def test_name_with_foreign_characters(self):
        self.assertEqual(generate_soundex("Renée"), "R500")
        
    def test_name_with_embedded_numbers(self):
        self.assertEqual(generate_soundex("R2D2"), "R300")
        
    def test_only_space(self):
        self.assertEqual(generate_soundex(" "), "")
        
    def test_repeated_vowels(self):
        self.assertEqual(generate_soundex("Aeeeiiiooo"), "A000")
        
    def test_name_with_leading_spaces(self):
        self.assertEqual(generate_soundex("  David"), "D130")
        
    def test_name_with_multiple_numbers(self):
        self.assertEqual(generate_soundex("123ABC456"), "A120")4
        
    def test_long_name(self):
        self.assertEqual(generate_soundex("Abcdefghijklmnop"), "A123")


if __name__ == '__main__':
    unittest.main()
