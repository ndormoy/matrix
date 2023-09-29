import math
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs, ft_max

from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix

"""
    https://www.sciencedirect.com/topics/mathematics/angle-between-two-vector#:~:text=The%20cosine%20of%20the%20angle%20between%20two%20nonzero%20vectors%20is,the%20product%20of%20their%20lengths.&text=Two%20vectors%20are%20orthogonal%20if,their%20dot%20product%20is%20zero.
    https://onlinemschool.com/math/library/vector/angl/
    cosine = (Dot [u, v]) / (Norm[u] Norm[v]);   --> We use Euclidian norm

    For example, if you have a vector v in two-dimensional space and you want to find the cosine of the angle it makes with the x-axis, you can calculate it as:

    cos(θ) = (v_x) / ||v||

    Where:

    θ is the angle between the vector v and the x-axis.
    v_x is the x-component of the vector v.
    ||v|| is the magnitude (norm) of the vector v.
    In this context, the cosine of the angle represents how much of the vector's length is aligned with the x-axis. If cos(θ) is 1, it means the vector is parallel to the x-axis. If it's 0, it means the vector is perpendicular to the x-axis. If it's -1, it means the vector is parallel but in the opposite direction of the x-axis.
"""
def angle_cos(u, v):
    dot_product = u.dot(v)
    norm_u = u.norm()
    norm_v = v.norm()
    
    if norm_u == 0.0 or norm_v == 0.0:
        return None  # Avoid division by zero
    if len(u.data) != len(v.data):
        raise None # different vector sizes
    return (dot_product / (norm_u * norm_v))