"""
Generators

Pros:
No list is created
Values don't need to be stored in memory simultaneously
"""

import numpy as np


def random_number_generator():
    for _ in range(10):
        x = np.random.randn()
        yield x


random_numbers = random_number_generator()
print(random_numbers)
for num in random_numbers:
    print(num)
