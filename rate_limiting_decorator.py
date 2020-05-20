""" Algorithm to limit the rate of incoming requests."""
import time
import unittest

# Decorator to limit incoming request as per the rate.
def my_rate_limiter_decorator(max_transaction, max_time):
  rate = max_transaction / max_time
  interval_within_per_second = 1.0 / float(rate)
  def my_rate_limiter(func):
    last_time_called = 0
    def wrapper(*args, **kwargs):
      nonlocal last_time_called
      try:
        elapsed_time = time.time() - last_time_called
        if elapsed_time < interval_within_per_second:
          time.sleep(interval_within_per_second - elapsed_time)
        func(*args, **kwargs)
      finally:
        last_time_called = time.time()
    return wrapper
  return my_rate_limiter

# Assuming we want 3 transactions per second.
@my_rate_limiter_decorator(3, 5)
def my_api():
  print('Hello.. You are using my service !!')


if __name__ == '__main__':
  for _ in range(0, 10):
    my_api()
