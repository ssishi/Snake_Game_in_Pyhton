from tkinter import LEFT
from turtle import left
import unittest
from io import StringIO
import Snake


class MyTestCase(unittest.TestCase):
    def test_previous(self):
        words = Snake.read_file('tests/test_list.txt')
        self.assertEqual(1, len(words))

class MyTestCase(unittest.TestCase):
    def test_user_input(self):
        delay = delay
        self.assertEqual(1,len(delay))


class MyTestCase(unittest.TestCase):
    def test_direction(self):
        LEFT = left
        self.assertEqual(2,)
        















        if __name__ == '__main__':
            unittest.main()