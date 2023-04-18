import json
import unittest
from main import getDictionaryContent

class TestGetDictionaryContent(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(getDictionaryContent(10), {'type': 'integer', 'tag': '', 'description': '', 'required': False})
    
    def test_string(self):
        self.assertEqual(getDictionaryContent('hello'), {'type': 'string', 'tag': '', 'description': '', 'required': False})
    
    def test_enum(self):
        self.assertEqual(getDictionaryContent(['one', 'two', 'three']), {'type': 'enum', 'tag': '', 'description': '', 'required': False})
    
    def test_array(self):
        self.assertEqual(getDictionaryContent([]), {'type': 'array', 'tag': '', 'description': '', 'required': False})
    
    def test_dict(self):
        self.assertEqual(getDictionaryContent({}), {'type': 'array', 'tag': '', 'description': '', 'required': False})
    
    def test_bool(self):
        self.assertEqual(getDictionaryContent(True), {'type': 'bool', 'tag': '', 'description': '', 'required': False})

if __name__ == '__main__':
    unittest.main()
