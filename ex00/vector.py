

"""_summary_

    This class represents a vector.
    The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
"""

class Vector:
    def __init__(self, data):
        self.data = data
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)
    
    def __str__(self):
        return str(self.data)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a numeric value.")
        return Vector([x * scalar for x in self.data])

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