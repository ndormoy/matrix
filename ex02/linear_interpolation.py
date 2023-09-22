import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from ex00.vector import Vector
from ex00.matrix import Matrix

"""
    Linear interpolation is a method for estimating values between two known values.
    It is a simple and commonly used technique to approximate a value that lies between two data points by assuming a linear relationship between them.

    In linear interpolation, you have two known data points (A and B) with values (y_A and y_B) and you want to find the value (y) at some point between A and B.
    Linear interpolation assumes that the relationship between the values is linear, which means that the change in the value is constant as you move from A to B.
"""


def lerp(u, v, t: float) -> Vector:
    """
        Linear interpolation between two vectors.
        Args:
            u: The first vector.
            v: The second vector.
            t: The interpolation parameter.

        Returns:
            The interpolated vector.
    """
    if type(u) != type(v):
        raise TypeError("u and v must have the same type.")
    elif t < 0 or t > 1:
        raise ValueError("t must be between 0 and 1.")
    elif isinstance(u, Vector):
        if len(u) != len(v):
            raise ValueError("Vector dimensions do not match.")
        return [round((1 - t) * ux + t * vy, 1) for ux, vy in zip(u, v)]
    elif isinstance(v, Matrix):
        if len(u.data) != len(v.data) or len(u.data[0]) != len(v.data[0]):
            raise ValueError("Matrix dimensions do not match.")
        return Matrix([
            [
                round((1 - t) * u_elem + t * v_elem, 1)
                for u_elem, v_elem in zip(u_row, v_row)
            ]
            for u_row, v_row in zip(u.data, v.data)
        ])
    return round((1 - t) * u + t * v, 1)
