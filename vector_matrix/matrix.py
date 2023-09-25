from vector_matrix.vector import Vector
import numpy as np



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
    

    """
        https://mathinsight.org/matrix_vector_multiplication

        For example, if
        A=[1 -1 2]
           0 -3 1
        and x=(2,1,0)
        , then
        Ax=[2⋅1 -1⋅1 + 0⋅2 ]
            2⋅0 -1⋅3 + 0⋅1
          = [1-3]
    """

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
        
        
    # https://www.statlect.com/matrix-algebra/trace-of-a-matrix
    # Is the sum of its diagonal entries
    def trace(self):
        if len(self.data) != len(self.data[0]):
            raise ValueError("Matrix must be square to calculate trace.")
        return sum(self.data[i][i] for i in range(len(self.data)))

    # https://www.cuemath.com/algebra/transpose-of-a-matrix/
    # The transpose of a matrix is a new matrix whose rows are the columns of the original.
    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(len(self.data))] for i in range(len(self.data[0]))])
    
    def shape(self):
        return (len(self.data), len(self.data[0]))
    
    """
        https://www.wikihow.com/Reduce-a-Matrix-to-Row-Echelon-Form
        https://saturncloud.io/blog/reducing-a-matrix-to-row-echelon-form-using-numpy-a-comprehensive-guide/
        Row echelon form :
        - Leading Entries: In each row of the matrix, the first nonzero element (from the left) is called a "leading entry," and it must be strictly to the right of the leading entry in the row just above it.
        - Zero Rows: Any rows consisting entirely of zeros are placed at the bottom of the matrix.
        - Columns of Leading Entries: The columns containing the leading entries must form a sequence of consecutive columns. In other words, there should be no columns between two leading entries.
        - Leading Entries are 1: Each leading entry must be equal to 1, which means that if a row contains a leading entry, it should be divided by that leading entry to make it 1.
        - Leading Entry Column Zeros: All entries below and above a leading entry must be zeros.
        - Leading Entry Rows Sorted: Rows with all zeros should be placed at the bottom, and the rows with leading entries should be ordered so that the leading entry in each row is to the right of the leading entry in the row just above it.
        
        1) num_rows, num_cols = len(self.data), len(self.data[0]): This line calculates the number of rows and columns in the matrix self. It uses the len function to determine the length of self.data, which represents the rows, and the length of self.data[0], which represents the number of columns.
        2) row = 0: Initialize a variable row to keep track of the current row during the row echelon form transformation. It starts at the first row (index 0).
        3) The method enters a loop that iterates over each column (col) from left to right.
        a. if row >= num_rows:: This condition checks whether we have processed all rows. If row is greater than or equal to the total number of rows (num_rows), it means we have completed the transformation for all rows, so the loop is exited using break.
        b. pivot_row = row: Initialize pivot_row to the current row row.
        c. while pivot_row < num_rows and self.data[pivot_row][col] == 0:: This loop searches for the first non-zero element in the current column (col). It keeps incrementing pivot_row until it finds a non-zero element or until it reaches the end of the matrix (num_rows). If it finds a non-zero element, the loop exits.
        d. if pivot_row == num_rows:: If the loop in step c didn't find a non-zero element in the current column, this condition checks if we've reached the end of the matrix (num_rows) without finding a non-zero element. If so, it means the column is all zeros, and we move to the next column by using continue, skipping the remaining code for the current column.
        e. self.swap_rows(pivot_row, row): If we found a non-zero element, we swap the rows to make this non-zero element the leading 1 (pivot element). This helps in creating the row echelon form. The swap_rows method is assumed to correctly swap the rows.
        f. pivot_element = self.data[row][col]: The pivot_element variable is assigned the value of the leading 1 (pivot element) in the current row (row) and current column (col).
        g. self.data[row] = [round(x / pivot_element, decimal_places) for x in self.data[row]]: We divide the entire row (self.data[row]) by the pivot_element to make it equal to 1. The round function is used to round each element in the row to the specified number of decimal places (decimal_places).
        h. Next, we eliminate other rows by subtracting multiples of the current row from them. This ensures that the leading 1 in the current column is the only non-zero element in that column.
        i. The loop variable row is incremented to move to the next row.
        4) After processing all columns and rows, the method returns self, which now contains the matrix in row echelon form.
    """
    
    def swap_rows(self, row1, row2):
        self.data[row1], self.data[row2] = self.data[row2], self.data[row1]
    
    def row_echelon(self, decimal_places=7):
        num_rows, num_cols = self.shape()

        row = 0

        for col in range(num_cols):
            if row >= num_rows:
                break

            # Find the first non-zero element in the current column
            pivot_row = row
            while pivot_row < num_rows and self.data[pivot_row][col] == 0:
                pivot_row += 1

            # If no non-zero element is found, move to the next column
            if pivot_row == num_rows:
                continue

            # Swap rows to make the pivot element the leading 1
            self.swap_rows(pivot_row, row)

            # Make the pivot element 1 and round it
            pivot_element = self.data[row][col]
            self.data[row] = [round(x / pivot_element, decimal_places) for x in self.data[row]]

            # Eliminate other rows
            for i in range(num_rows):
                if i != row:
                    factor = self.data[i][col]
                    self.data[i] = [round(x - factor * y, decimal_places) for x, y in zip(self.data[i], self.data[row])]

            row += 1

        return self

    