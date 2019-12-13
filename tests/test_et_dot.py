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