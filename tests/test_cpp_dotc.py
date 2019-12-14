#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for C++ module ET-dot.dotc.
"""

# import our binary extension
import et_dot # this may engage auto-build
cpp = et_dot.dotc

import numpy as np


def test_dotc_aa():
    a = np.array([0, 1, 2, 3, 4], dtype=np.float)
    expected = np.dot(a, a)
    a_dotc_a = cpp.dotc(a, a)
    assert a_dotc_a == expected


#===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
#===============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_dotc_aa

    print(f"__main__ running {the_test_you_want_to_debug} ...")
    the_test_you_want_to_debug()
    print('-*# finished #*-')
#===============================================================================
