

"""_summary_

    This class represents a vector.
    The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
"""

class Vector:
    def __init__(self, data):
        self.data = data

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

    def __str__(self):
        return str(self.data)