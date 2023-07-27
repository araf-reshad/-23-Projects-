import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_docstring_display_score(self):
      s1 = 'def display_score():'
      s2 = '"""Simulates one round of rock-paper-scissors.'
      with open("main.py", "r") as f:
        lines  = [line.strip() for line in f.readlines()]
        f_line_num = 0
        for line_num in range(len(lines)):
          if lines[line_num] == s1:
            f_line_num = line_num
            break
        if lines[f_line_num + 1] != s2:
          self.fail()
    

