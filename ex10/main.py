import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 10 : MATRIX row echelon form ✅\n", "green")
    colorize_text("MATRIX\n", "purple")

    try:
        u1_data = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        ]

        u2_data = [
            [1.0, 2.0],
            [3.0, 4.0],
        ]

        u3_data = [
            [1.0, 2.0],
            [2.0, 4.0],
        ]

        u4_data = [
            [8.0, 5.0, -2.0, 4.0, 28.0],
            [4.0, 2.5, 20.0, 4.0, -4.0],
            [8.0, 5.0, 1.0, 4.0, 17.0],
        ]

        u1 = Matrix(u1_data)
        u2 = Matrix(u2_data)
        u3 = Matrix(u3_data)
        u4 = Matrix(u4_data)

        colorize_text("row echelon of [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]", "yellow")
        print(f"{u1.row_echelon()}\n")
        # [1.0, 0.0, 0.0]
        # [0.0, 1.0, 0.0]
        # [0.0, 0.0, 1.0]
        
        colorize_text("row echelon of [[1.0, 2.0], [3.0, 4.0]]", "yellow")
        print(f"{u2.row_echelon()}\n")
        # [1.0, 0.0]
        # [0.0, 1.0]
        
        colorize_text("row echelon of [[1.0, 2.0], [2.0, 4.0]]", "yellow")
        print(f"{u3.row_echelon()}\n")
        # [1.0, 2.0]
        # [0.0, 0.0]
        
        colorize_text("row echelon of [[8.0, 5.0, -2.0, 4.0, 28.0], [4.0, 2.5, 20.0, 4.0, -4.0], [8.0, 5.0, 1.0, 4.0, 17.0]]", "yellow")
        print(f"{u4.row_echelon()}\n")
        # [1.0, 0.625, 0.0, 0.0, -12.1666667]
        # [0.0, 0.0, 1.0, 0.0, -3.6666667]
        # [0.0, 0.0, 0.0, 1.0, 29.5 ]


    except Exception as e:
        print(e)
        
    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")
    
    try:
        colorize_text("row echelon of [[0, 0], [0, 0]]", "yellow")
        u5 = Matrix([[0, 0], [0, 0]])
        print(f"{u5.row_echelon()} \nexpected :\n[[0, 0], [0, 0]]\n")
    
        colorize_text("row echelon of [[1, 0], [0, 0]]", "yellow")
        u6 = Matrix([[1, 0], [0, 1]])
        print(f"{u6.row_echelon()} \nexpected :\n[[1, 0], [0, 1]]\n")
        
        colorize_text("row echelon of [[4, 2], [2, 1]]", "yellow")
        u7 = Matrix([[4, 2], [2, 1]])
        print(f"{u7.row_echelon()} \nexpected :\n[[1, 0.5], [0, 0]]\n")
        
        colorize_text("row echelon of [[-7, 2], [4, 8]]", "yellow")
        u8 = Matrix([[-7, 2], [4, 8]])
        print(f"{u8.row_echelon()} \nexpected :\n[[1, 0], [0, 1]]\n")
        
        colorize_text("row echelon of [[1, 2], [4, 8]]", "yellow")
        u9 = Matrix([[1, 2], [4, 8]])
        print(f"{u9.row_echelon()} \nexpected :\n[[1, 2], [0, 0]]\n")
    
    except Exception as e:
        print(e) 

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
