"""
    Parallel system transfer function

    G(c) = [s + 1 / s + 2]
    G(s) = 1/ 500s^2

    T(s)  = G(c) || G(s)
"""
from ..utils.display import td

import control as ct
import numpy as np


def parallelize():
    """
        Generates a system of transfer functions for
        a parallel block combination
    """

    # Create arrays for G(s)
    numerator_g = np.array([1])
    denominator_g = np.array([500, 0, 0])

    # Create arrays for G(c)
    numerator_h = np.array([1, 1])
    denominator_h = np.array([1, 2])

    # Get transfer functions
    sys_g = ct.tf(numerator_g, denominator_g)
    sys_h = ct.tf(numerator_h, denominator_h)
    sys_tranfer_func = ct.parallel(sys_g, sys_h)

    td.ouput('Parallel TF', keys=['G(s)', 'G(c)', 'sys tf'],
             values=[sys_g, sys_h, sys_tranfer_func])


if __name__ == '__main__':
    parallelize()
