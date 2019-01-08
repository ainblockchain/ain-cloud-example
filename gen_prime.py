# Example python code for demonstrating AIN Cloud Beta.
#
# This code prints out all the prime numbers found in the given range.

def is_prime_number(num):
  if num < 2:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

def gen_prime_number(max_val):
  for i in range(max_val):
    if is_prime_number(i):
      print(i)

gen_prime_number(100)
