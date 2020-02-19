#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """
""" """

__author__ = "Patrick Buzzo"


def add(x, y):
    new_num = x + y
    return new_num


def multiply(x, y):
    new_num = 0
    if y >= 0:
        for index in range(y):
            new_num += x
    else:
        for index in range(-y):
            new_num -= x
    return new_num
    # new_num = 0
    # count = 0
    # if (x < 0) and (y >= 0):
    #     while count < y:
    #         new_num = new_num + x
    #         count += 1
    # elif (x >= 0) and (y < 0):
    #     y = -y
    #     while count < y:
    #         new_num = new_num + x
    #         count += 1
    # elif (x >= 0) and (y >= 0):
    #     while count < y:
    #         new_num = new_num + x
    #         count += 1
    # elif (x < 0) and (y < 0):
    #     x = -x
    #     y = -y
    #     while count < y:
    #         new_num = new_num + x
    #         count += 1
    # return new_num


def power(x, n):
    """Raise x to power n, where n >= 0"""
    if n == 0:
        return 1
    elif x == 0:
        return 0
    else:
        new_num = x
        if n == 1:
            return x
        else:
            for index in range(n-1):
                new_num = multiply(new_num, x)
    return new_num


def factorial(x):
    """Compute factorial of x, where x > 0"""
    new_num = x
    if x == 0 or x == 1:
        return 1
    if x > 1:
        count = x - 1
        while count > 0:
            new_num = multiply(new_num, count)
            count -= 1
    return new_num


def fibonacci(n):
    """Compute the nth term of fibonacci sequence
    Resources: http://bit.ly/2P5asH2 , http://bit.ly/2vOJDji
    """
    a, b = 0, 1
    for index in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    # your code to call functions above
    pass
