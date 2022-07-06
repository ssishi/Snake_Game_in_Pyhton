import unittest
from io import StringIO
import Snake


class MyTestCase(unittest.TestCase):
    def test_previous(self):
        words = Snake.read_file('tests/test_list.txt')
        self.assertEqual(1, len(words))















        if __name__ == '__main__':
            unittest.main()