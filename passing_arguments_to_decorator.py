def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
  def decorator(func):
    def wrapper(function_arg1, function_arg2, function_arg3):
      "This is the wrapper function"
      print("The wrapper can access all the variables\n"
            "\t- from the decorator maker: {0} {1} {2}\n"
            "\t- from the function call: {3} {4} {5}\n"
            "and pass them to the decorated function"
            .format(decorator_arg1, decorator_arg2, decorator_arg3,
                    function_arg1, function_arg2, function_arg3))
      func(function_arg1, function_arg2, function_arg3)
    return wrapper
  return decorator

pandas = "Pandas"


@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
  print("This is the decorated function and it only knows about its arguments: {0}"
        " {1}" " {2}".format(function_arg1, function_arg2, function_arg3))


if __name__ == '__main__':
  decorated_function_with_arguments(pandas, "Science", "Tools")

"""Expected output on the screen:-
The wrapper can access all the variables
	- from the decorator maker: Pandas Numpy Scikit-learn
	- from the function call: Pandas Science Tools
and pass them to the decorated function
This is the decorated function and it only knows about its arguments: Pandas Science Tools
"""