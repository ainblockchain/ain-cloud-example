# ain-cloud-example on AIN

You can run **ain-cloud-example** code on [`AIN Cloud beta`](https://cloud.ainetwork.ai/), which is a product provided by [`AI Network`](https://ainetwork.ai/).

## How to get ready to use AIN Cloud beta

The payment in [`AIN Cloud beta`](https://cloud.ainetwork.ai/) is done based on AIN Ethereum Token (Token Symbol: *AIN*), so you need to prepare some account balance before getting started.
Fortunately, AIN Cloud beta provides welcome bonus for new users. Please refer to *AIN Cloud beta Guide (coming soon)* for the details.
In summary, 1) sign up on [`cloud.ainetwork.ai/`](https://cloud.ainetwork.ai/) and finish the email verification step to get sign-up bonus (~ 150 AIN) and 2) complete KYC process on [`cloud.ainetwork.ai/buyain`](https://cloud.ainetwork.ai/buyain) to get extra bonus (~ 150 AIN).

## How to play with ain-cloud-example code on AIN Cloud beta

### gen_prime.py

This is naive python source code to generate all the prime numbers in given range.
Try to run the code by pressing the "Run" button [`AIN Cloud beta`](https://cloud.ainetwork.ai/)
and see if it gives correct answers:

```bash
# Example python code for demonstrating AIN Cloud beta.
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
```

The expected output is the prime numbers generated:

```bash
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```

Try to modify the code to improve the performance.
