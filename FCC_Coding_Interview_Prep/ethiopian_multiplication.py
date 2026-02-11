# Required to break this out into four separate functions

import functools


def eth_mult(a, b):
    halved = halving(a)
    doubled = doubling(halved, b)
    evened = is_even(halved, doubled)
    return functools.reduce(lambda x, y: x + y, evened)


def halving(a):
    temp_a = a
    a_array = [a]
    while temp_a > 1:
        temp_a //= 2
        a_array.append(temp_a)
    return a_array


def doubling(a_array, b):
    temp_b = b
    b_array = []
    for i in range(len(a_array)):
        b_array.append(temp_b * (2 ** i))
    return b_array


def is_even(a_array, b_array):
    c_array = [a_array.index(a) for a in a_array if a % 2 != 0]
    d_array = [b_array[index] for index in c_array]
    return d_array
# Alternatively, and more simply:
#   c_array = [v for (k, v) in zip(a_array, b_array) if k % 2 != 0]
#   return c_array


print(eth_mult(63, 74))
