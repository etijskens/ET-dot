#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for f2py module `et_dot.dotf`."""

import numpy as np

# import the binary extension and rename the module locally as f90
import et_dot
f90 = et_dot.dotf


def test_dotf_aa():
    a = np.array([0, 1, 2, 3, 4], dtype=np.float)
    expected = np.dot(a, a)
    a_dotf_a = f90.dotf(a, a)
    assert a_dotf_a == expected


#===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
#===============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_dotf_aa

    print(f"__main__ running {the_test_you_want_to_debug} ...")
    the_test_you_want_to_debug()
    print('-*# finished #*-')
#===============================================================================
