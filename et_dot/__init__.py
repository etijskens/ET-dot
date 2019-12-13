# -*- coding: utf-8 -*-
"""
Package et_dot
==============
Python module for computing the dot product of two arrays.
"""
__version__ = "0.0.6"


def dot(a, b):
    """Compute the dot product of *a* and *b*.

    :param a: a 1D array.
    :param b: a 1D array of the same length as *a*.
    :returns: the dot product of *a* and *b*.
    :raises: ArithmeticError if ``len(a)!=len(b)``.
    """
    n = len(a)
    if len(b) != n:
        raise ArithmeticError("dot(a,b) requires len(a)==len(b).")
    d = 0
    for i in range(n):
        d += a[i] * b[i]
    return d
