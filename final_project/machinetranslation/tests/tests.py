import unittest
from translator import french_to_english
from translator import english_to_french

class testTranslator(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english('Comment vas-tu?'),'How are you?')
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('None'),'')
        self.assertEqual(french_to_english(0),0)

class testTranslator1(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('How are you?'),'Comment vas-tu?')
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('None'),'')
        self.assertEqual(english_to_french(0),0)

unittest.main()