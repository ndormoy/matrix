import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 11 : MATRIX Determinant ✅\n", "green")
    colorize_text("MATRIX\n", "purple")
    
    try:
        colorize_text("determinant of [[1.0, -1.0], [-1.1, 1.0]]", "yellow")
        # Matrix u1
        u1_data = [
            [1.0, -1.0],
            [-1.0, 1.0],
        ]
        u1 = Matrix(u1_data)
        print(f"{u1.determinant()} --> expected : 0.0\n")

        colorize_text("determinant of [[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]]", "yellow")
        # Matrix u2
        u2_data = [
            [2.0, 0.0, 0.0],
            [0.0, 2.0, 0.0],
            [0.0, 0.0, 2.0],
        ]
        u2 = Matrix(u2_data)
        print(f"{u2.determinant()} --> expected : 8.0\n")

        colorize_text("determinant of [[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]]", "yellow")
        # Matrix u3
        u3_data = [
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0],
        ]
        u3 = Matrix(u3_data)
        print(f"{u3.determinant()} --> expected : -174.0\n")

        colorize_text("determinant of [[8.0, 5.0, -2.0, 4.0], [4.0, 2.5, 20.0, 4.0], [8.0, 5.0, 1.0, 4.0], [28.0, -4.0, 17.0, 1.0]]", "yellow")
        # Matrix u4
        u4_data = [
            [8.0, 5.0, -2.0, 4.0],
            [4.0, 2.5, 20.0, 4.0],
            [8.0, 5.0, 1.0, 4.0],
            [28.0, -4.0, 17.0, 1.0],
        ]
        u4 = Matrix(u4_data)
        print(f"{u4.determinant()} --> expected : 1032.0\n")
        
    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : \n", "red")
    try:
        colorize_text("determinant of [[8.0, 5.0, -2.0, 4.0],4.0, 2.5, 20.0, 4.0],[8.0, 5.0, 1.0, 4.0],[28.0, -4.0, 17.0, 1.0],[25.0, -2.0, 1.0, 16.0],]", "yellow")
        u5_data = [
            [8.0, 5.0, -2.0, 4.0],
            [4.0, 2.5, 20.0, 4.0],
            [8.0, 5.0, 1.0, 4.0],
            [28.0, -4.0, 17.0, 1.0],
            [25.0, -2.0, 1.0, 16.0],
        ]
        u5 = Matrix(u5_data)
        print(f"{u5.determinant()}\n")

    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : ", "red")
    try:
        colorize_text("[[8.0, 5.0, -2.0, 4.0, 5.0],[4.0, 2.5, 20.0, 4.0, 4.0],[8.0, 5.0, 1.0, 4.0, 1.0],[28.0, -4.0, 17.0, 1.0, 7.0],[2.0, -26.0, 14.0, 6.0, 9.0],]", "yellow")
        u6_data = [
            [8.0, 5.0, -2.0, 4.0, 5.0],
            [4.0, 2.5, 20.0, 4.0, 4.0],
            [8.0, 5.0, 1.0, 4.0, 1.0],
            [28.0, -4.0, 17.0, 1.0, 7.0],
            [2.0, -26.0, 14.0, 6.0, 9.0],
        ]
        u6 = Matrix(u6_data)
        print(f"{u6.determinant()}")

    except Exception as e:
        print(e)

    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")
    
    try:
        colorize_text("determinant of [[0, 0], [0, 0]]", "yellow")
        u7 = Matrix([[0, 0], [0, 0]])
        print(f"{u7.determinant()} --> expected : 0\n")
        
        colorize_text("determinant of [[1, 0], [0, 1]]", "yellow")
        u8 = Matrix([[1, 0], [0, 1]])
        print(f"{u8.determinant()} --> expected : 1\n")
        
        colorize_text("determinant of [[2, 0], [0, 2]]", "yellow")
        u9 = Matrix([[2, 0], [0, 2]])
        print(f"{u9.determinant()} --> expected : 4\n")
        
        colorize_text("determinant of [[1, 1], [1, 1]]", "yellow")
        u10 = Matrix([[1, 1], [1, 1]])
        print(f"{u10.determinant()} --> expected : 0\n")
        
        colorize_text("determinant of [[0, 1], [1, 0]]", "yellow")
        u11 = Matrix([[0, 1], [1, 0]])
        print(f"{u11.determinant()} --> expected : -1\n")
        
        colorize_text("determinant of [[1, 2], [3, 4]]", "yellow")
        u12 = Matrix([[1, 2], [3, 4]])
        print(f"{u12.determinant()} --> expected : -2\n")
        
        colorize_text("determinant of [[-7, 5], [4, 6]]", "yellow")
        u13 = Matrix([[-7, 5], [4, 6]])
        print(f"{u13.determinant()} --> expected : -62\n")
        
        colorize_text("determinant of [[1, 0, 0], [0, 1, 0], [0, 0, 1]]", "yellow")
        u14 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        print(f"{u14.determinant()} --> expected : 1\n")
        
        
    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
