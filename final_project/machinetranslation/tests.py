import unittest
from translator import french_to_english
from translator import english_to_french

class testTranslator(unittest.TestCase):
    def test_f2e(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('None'),'')
        
class testTranslator1(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'),'')
        
unittest.main()