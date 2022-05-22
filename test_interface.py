import unittest
import interface



class TestInterface(unittest.TestCase):

    def test_url_parse(self):
        result = interface.view_shop("http://127.0.0.1:8000/products_list")
        self.assertIs(result, "http://127.0.0.1:8000/products_list")

if __name__ == '__main__':
    unittest.main()