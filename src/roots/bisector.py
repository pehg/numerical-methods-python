import numpy as np
import logging


def bisector_method(f, a, b, n_iters=100, tolerance=0.000000000001):
    '''
    Find root of a continuous function in the interval [a, b].

    Tries to find f(x)=0 on the interval [a, b].

    Args:
        f (function): Python function. Should accept one argument and return one value.
                      Represents a continuous function.
        a (float): left limit of the interval
        b (float): right limit of the interval
        tolerance (float, opt): By default is 1E-12
        n_iter (int): Number of iterations to try to find the root. Must be positive.

    Return:
        float or Exception
        If the solution is found, return a float. Returns an Exception otherwise.

    Notes:
        This algorithm was obtained from https://www.youtube.com/watch?v=mGULVFGqCHA&list=PL-xEHa0Tmq2w0vLOjmjFkbTUArmHFzbQV&index=4
    '''
    original_a = a
    original_b = b
    original_n_iters = n_iters

    f_a = f(a)
    i = 0
    while i < n_iters:
        delta = (b - a) / 2.0
        c = a + delta
        f_c = f(c)

        logging.debug(f"a: {a:4.9f}, c: {c:4.9f}, b: {b:4.9f} --- f(a): {f_a:4.9f}, f(c): {f_c:4.9f}, f(b): {f(b):4.9f}")

        # Check if we found it
        if np.abs(f_c) < tolerance or np.abs(delta) < tolerance:
            return c

        if (f_a * f_c) >= 0:
            # No change of sign. The next iteration we only check the range [c, b], in which c will become the new a
            a = c
            f_a = f_c
        else:
            # There's a change in sing. The next iteration check only the range [a, c] in which c will become the next b
            b = c

        i += 1

    # If we get here, we failed to find the root
    return Exception('Cannot find a root in the interval [{}, {}] in {} iterations. Last point c={}, f(c)={}'.format(original_a, original_b, original_n_iters, c, f_c))
