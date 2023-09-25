import math
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from ex00.vector import Vector
from ex00.matrix import Matrix

# https://www.sciencedirect.com/topics/mathematics/angle-between-two-vector#:~:text=The%20cosine%20of%20the%20angle%20between%20two%20nonzero%20vectors%20is,the%20product%20of%20their%20lengths.&text=Two%20vectors%20are%20orthogonal%20if,their%20dot%20product%20is%20zero.
# https://onlinemschool.com/math/library/vector/angl/
# cosine = (Dot [u, v]) / (Norm[u] Norm[v]);   --> We use Euclidian norm
def angle_cos(u, v):
    dot_product = u.dot(v)
    norm_u = u.norm()
    norm_v = v.norm()
    
    if norm_u == 0.0 or norm_v == 0.0:
        return None  # Avoid division by zero
    if len(u.data) != len(v.data):
        raise None # different vector sizes
    return round(dot_product / (norm_u * norm_v), 9)