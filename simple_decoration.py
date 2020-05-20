import unittest

# Refer https://www.datacamp.com/community/tutorials/decorators-python
def uppercase_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper

# Using uppercase decorator
@uppercase_decorator
def say_hi():
  return 'hello there'

# Appy multiple decorators to a method
def split_string(function):
    def wrapper():
      func = function()
      splitted_string = func.split()
      return splitted_string
    return wrapper

@split_string
@uppercase_decorator
def say_split_hi():
    return 'hello there'

class TestMyDecorators(unittest.TestCase):
  def test_say_hi(self):
    self.assertEqual(say_hi(), 'HELLO THERE')

  def test_split_hi(self):
    self.assertListEqual(say_split_hi(), ['HELLO', 'THERE'])
