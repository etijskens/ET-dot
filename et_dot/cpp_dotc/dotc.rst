Module et_dot.dotc
******************

Module :py:mod:`dotc` built from fortran code in :file:`cpp_dotc/dotc.cpp`.

.. function:: dotc(a,b)
  :module: et_dot.dotc

  Compute the dot product of *a* and *b* (in C++.)

  :param a: 1D Numpy array with ``dtype=numpy.float64``
  :param b: 1D Numpy array with ``dtype=numpy.float64``
  :returns: the dot product of *a* and *b*
  :rtype: ``numpy.float64``

