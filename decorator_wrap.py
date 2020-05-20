"""Decorators wrap functions, The original function name, its docstring, and parameter list
are all hidden by the wrapper closure.
To Solve this, Python provides a functools.wraps decorator.
This decorator copies the lost metadata
from the undecorated function to the decorated closure.
Let's show how we'd do that."""

import functools
import unittest

def uppercase_decorator(func):
  @functools.wraps(func)
  def wrapper():
    return func().upper()
  return wrapper

@uppercase_decorator
def say_hi():
  "This will say hi"
  return 'hello there'

class TestMyWrapDecorators(unittest.TestCase):
  def test_say_hi(self):
    self.assertEqual(say_hi(), 'HELLO THERE')
