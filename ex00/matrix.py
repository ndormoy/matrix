

"""_summary_

    This class represents a matrix.
    len(self.data) != len(other.data) -> check if the number of rows are the same length
    len(self.data[0]) != len(other.data[0]) -> check if the number of columns are the same length
"""

class Matrix:
    def __init__(self, data):
        self.data = data

    def add(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrix dimensions do not match.")
        self.data = [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)]

    def sub(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrix dimensions do not match.")
        self.data = [[x - y for x, y in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)]

    def scl(self, scalar):
        self.data = [[x * scalar for x in row] for row in self.data]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Division by zero is not allowed.")
        return Matrix([[x / scalar for x in row] for row in self.data])