# -*- coding: utf-8 -*-

"""Tests for et_dot package."""

import random

import et_dot


def test_dot_aa():
    a = [1, 2, 3]
    expected = 14
    result = et_dot.dot(a, a)
    assert result == expected


def test_dot_commutative():
    # create two arrays of length 10 with random float numbers:
    a = []
    b = []
    for _ in range(10):
        a.append(random.random())
        b.append(random.random())
    # do the test
    ab = et_dot.dot(a,b)
    ba = et_dot.dot(b,a)
    assert ab==ba

def test_dot_commutative_2():
    # Fix the seed for the random number generator of module random.
    random.seed(0)
    # choose array size
    n = 10
    # create two arrays of length n with with zeros:
    a = n * [0]
    b = n * [0]
    # repetion loop:
    for r in range(1000):
        # fill a and b with random float numbers:
        for i in range(n):
           a[i] = random.random()
           b[i] = random.random()
        # do the test
        ab = et_dot.dot(a,b)
        ba = et_dot.dot(b,a)
        assert ab==ba


def test_dot_zero():
    # Fix the seed for the random number generator of module random.
    random.seed(0)
    # choose array size
    n = 10
    # create two arrays of length n with with zeros:
    a = n * [0]
    zero = n * [0]
    # repetion loop (the underscore is a placeholder for a variable dat we do not use):
    for _ in range(1000):
        # fill a with random float numbers:
        for i in range(n):
            a[i] = random.random()
        # do the test
        azero = et_dot.dot(a, zero)
        assert azero == 0


def test_dot_one():
    # Fix the seed for the random number generator of module random.
    random.seed(0)
    # choose array size
    n = 10
    # create two arrays of length n with with zeros:
    a = n * [0]
    one = n * [1.0]
    # repetion loop (the underscore is a placeholder for a variable dat we do not use):
    for _ in range(1000):
        # fill a with random float numbers:
        for i in range(n):
            a[i] = random.random()
        # do the test
        aone = et_dot.dot(a, one)
        expected = sum(a)
        assert aone == expected


def test_dot_one_2():
    a1 = 1.0e16
    a = [a1, 1.0, -a1]
    one = [1.0, 1.0, 1.0]
    expected = 1.0
    result = et_dot.dot(a, one)
    assert result == expected


# ==============================================================================
# The code below is for debugging a particular test.
# (otherwise all tests are normally run with pytest).
# Make sure that you run this code with the project directory as CWD, and
# that the source directory is on the path
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_dot_aa

    print("__main__ running", the_test_you_want_to_debug)
    the_test_you_want_to_debug()
    print('-*# finished #*-')
    
# eof