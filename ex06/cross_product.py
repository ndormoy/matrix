import math
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from ex00.vector import Vector
from ex00.matrix import Matrix

# https://www.mathsisfun.com/algebra/vectors-cross-product.html
# When a and b start at the origin point (0,0,0), the Cross Product will end at:
# cx = aybz − azby
# cy = azbx − axbz
# cz = axby − aybx

def cross_product(u, v):
    if len(u.data) != 3 or len(v.data) != 3:
        raise ValueError("Both vectors must have exactly three elements for cross product.")

    result = [
        u.data[1] * v.data[2] - u.data[2] * v.data[1],
        u.data[2] * v.data[0] - u.data[0] * v.data[2],
        u.data[0] * v.data[1] - u.data[1] * v.data[0]
    ]

    return Vector(result)