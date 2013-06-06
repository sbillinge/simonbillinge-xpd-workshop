#!/usr/bin/env python


"""Function that returns roots for a second degree polynomial.
"""

import cmath


def solveQuadraticRoots(A, B, C):
    """Find roots of a quadratic polynomial A*x**2 + B*x + C
    
    Parameters
    ----------
    arglist:
    A: float-like
       coefficient of x**2 term
    B: float-like
       coefficient of x term
    C: float-like
       constant
    
    Returns
    -------
    two roots of the equation, x1 and x2
    
    """
    det = cmath.sqrt(B**2 - 4 * A * C)
    x1 = (-B + det) / (2 * A)
    x2 = (-B - det) / (2 * A)
    return [x1, x2]
