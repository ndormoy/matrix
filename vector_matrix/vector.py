import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.math import ft_abs, ft_max

"""_summary_

    This class represents a vector.
    The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
"""

class Vector:
    def __init__(self, data):
        self.data = data
        # # Check if all elements in both vectors are of type float
        # if not all(isinstance(x, float) for x in self.data):
        #     raise ValueError("All elements in both vectors must be of type float.")
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)
    
    def __str__(self):
        return str(self.data)
    
    # def __mul__(self, scalar):
    #     if not isinstance(scalar, (int, float)):
    #         raise TypeError("Scalar must be a numeric value.")
    #     return Vector([x * scalar for x in self.data])

    def add(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Vector dimensions do not match.")
        self.data = [x + y for x, y in zip(self.data, other.data)]

    def sub(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Vector dimensions do not match.")
        self.data = [x - y for x, y in zip(self.data, other.data)]

    def scl(self, scalar):
        self.data = [x * scalar for x in self.data]
        # return Vector([x * scalar for x in self.data])

    def dot(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Vector dimensions do not match.")
        # Check if all elements in both vectors are of type float
        if not all(isinstance(x, float) for x in self.data) or not all(isinstance(x, float) for x in other.data):
            raise ValueError("All elements in both vectors must be of type float.")
        return sum(x * y for x, y in zip(self.data, other.data))


    #! https://montjoile.medium.com/l0-norm-l1-norm-l2-norm-l-infinity-norm-7a7d18a4f40c
    
    # norm1 ( Manhattan Distance or Taxicab norm) : 
    # the sum of absolute difference of the components of the vectors.
    def norm_1(self):
        return sum(ft_abs(x) for x in self.data)
    
    # norm2 (Euclidean norm) :
    # It is the shortest distance to go from one point to another.
    def norm(self):
        return sum((ft_abs(x))**2 for x in self.data)**0.5
    
    # infinity norm : Gives the largest magnitude among each element of a vector.
    # Having the vector X= [-6, 4, 2], the L-infinity norm is 6.
    # def norm_inf(self):
    #     return max(ft_abs(x) for x in self.data)
    def norm_inf(self):
        # Convert the generator expression to a list
        abs_values = [ft_abs(x) for x in self.data]

        # Use the ft_max function on the list
        return ft_max(abs_values)