/*
 *  C++ source file for module et_dot.dotc
 */


// See http://people.duke.edu/~ccc14/cspy/18G_C++_Python_pybind11.html for examples on how to use pybind11.

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

double
dotc( pybind11::array_t<double> a
    , pybind11::array_t<double> b
    )
{
    auto bufa = a.request()
       , bufb = b.request()
       ;
 // verify dimensions and shape:
    if( bufa.ndim != 1 || bufb.ndim != 1 ) {
        throw std::runtime_error("Number of dimensions must be one");
    }
    if( (bufa.shape[0] != bufb.shape[0]) ) {
        throw std::runtime_error("Input shapes must match");
    }
 // provide access to raw memory
 // because the Numpy arrays are mutable by default, py::array_t is mutable too.
 // Below we declare the raw C++ arrays for x and y as const to make their intent clear.
    double const *ptra = static_cast<double const *>(bufa.ptr);
    double const *ptrb = static_cast<double const *>(bufb.ptr);

    double d = 0.0;
    for (size_t i = 0; i < bufa.shape[0]; i++)
        d += ptra[i] * ptrb[i];

    return d;
}

// describe what goes in the module
PYBIND11_MODULE(dotc, m)
{// optional module docstring:
    m.doc() = "pybind11 dotc plugin";
 // list the functions you want to expose:
 // m.def("exposed_name", function_pointer, "doc-string for the exposed function");
    m.def("dotc", &dotc, "The dot product of two arrays 'a' and 'b'.");
}

