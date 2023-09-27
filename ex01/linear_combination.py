
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from vector_matrix.vector import Vector

def linear_combination(u : Vector, coefs) -> Vector:
    """
        Return the linear combination of the provided vectors using the provided coefficients.

        Parameters:
            vectors (list[Vector]): The vectors to combine.
            coefficients (list[float]): The coefficients to use.
    """
    if len(u) != len(coefs):
        raise ValueError("The number of vectors and coefficients must be the same.")

    # This loop iterates through each pair of input vectors and coefficients using zip, and adds them together.
    result = Vector([0.0 for _ in range(len(u[0].data))])
    for vector, coefficient in zip(u, coefs):
        scaled_vector = Vector([x * coefficient for x in vector.data])
        result.add(scaled_vector)

    return result
