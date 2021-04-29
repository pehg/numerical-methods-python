# To run this test, in the terminal run
#     python -m pytest .\tst\test_bisector.py
# The difference between calling
#     pytest path/test_file.py
# and
#     python -m pytest path/test_file.py
# is that the latter adds the current directory to sys.path
#
# Obtained from https://docs.pytest.org/en/latest/explanation/pythonpath.html#pytest-vs-python-m-pytest

import pytest
import src.roots.bisector as bsct
import numpy as np


class Args:
    def __init__(self, func, a, b, n_iters, tol=0.000000000001):
        self.f = func
        self.a = a
        self.b = b
        self.n_iters = n_iters
        self.tol = tol

    def __repr__(self):
        return f'Args({self.f}, {self.a}, {self.b}, {self.n_iters}, {self.tol})'


def test_bisector_method():
    EPS = 0.000000000001    # 1E-12

    def f1(x):
        """
        f1(x) = (x-2)^2
        roots: x=2
        """
        return np.power(x-2, 2)

    def f2(x):
        """
        f2(x) = ((x/2)-3)^2 - 1
        roots: x=4, x=8
        # 2(+-1 + 3) = 8, 4
        """
        return np.power((x/2)-3, 2) - 1


    test_cases = [(Args(f1, 0.5, 2.1, 100), 2.0),
                  (Args(f2, 3.9, 5.6, 100), 4),
                  (Args(f2, 4.1, 16.2, 100), 8)]


    for args, ans in test_cases:
        print(args)
        sol = None
        try:
            sol = bsct.bisector_method(args.f, args.a, args.b, args.n_iters)
            assert abs(sol - ans) < EPS
        except:
            raise sol


