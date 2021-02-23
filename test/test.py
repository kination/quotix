from unittest import TestCase
from src.file import replace_quotes

class Test(TestCase):
    def setUp(self):
        print('setup test')

    def tearDown(self):
        print('teardown test')

    def test_replace(self):
        replace_quotes('test/sample/dummy.py', 'double-to-single')


if __name__ == '__main__':
    unittest.main()
