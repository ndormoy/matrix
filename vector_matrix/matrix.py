from vector_matrix.vector import Vector


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
    

    # https://mathinsight.org/matrix_vector_multiplication

    # For example, if
    # A=[1 −1 2]
    #    0 −3 1
    # and x=(2,1,0)
    # , then
    # Ax=[2⋅1 −1⋅1 + 0⋅2 ]
    #     2⋅0 −1⋅3 + 0⋅1
    #   = [1−3]

    def mul_vec(self, vec) -> Vector:
        if len(self.data[0]) != len(vec.data):
            raise ValueError("Matrix columns must match vector dimensions for multiplication.")

        result = [sum(self.data[i][j] * vec.data[j] for j in range(len(vec.data))) for i in range(len(self.data))]
        return Vector(result)

    
    def mul_mat(self, matrix2):
        # print(f"pouet {len(self.data[0])}, {len(matrix2.data)}")
        if len(self.data[0]) != len(matrix2.data):
            # print(f"FAILED {len(self.data[0])}, {len(matrix2.data)}")
            raise ValueError("Matrix1 columns must match Matrix2 rows for multiplication.")

        result = [[sum(self.data[i][j] * matrix2.data[j][k] for j in range(len(matrix2.data))) for k in range(len(matrix2.data[0]))] for i in range(len(self.data))]
        return Matrix(result)
        
        
    