"""
Taylor series
"""
import math
from typing import Union
from itertools import count

EPSILON = 0.0001


def get_item_n(x, n):
    return x**n / math.factorial(n)


def get_sin(x, n):
    return ((-1)**n) * (x**(2*n + 1)) / math.factorial((2*n)+1)


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    sum_ = 1
    for n in count(1, 1):
        current_item = get_item_n(x, n)
        sum_ += current_item
        if current_item <= EPSILON:
            return sum_

    return sum_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sum_ = 0
    for n in count(0, 1):
        concurrent_item = get_sin(x, n)
        print(concurrent_item)
        sum_ += concurrent_item

        if abs(concurrent_item) <= EPSILON:
            break

    print(x)
    return sum_
