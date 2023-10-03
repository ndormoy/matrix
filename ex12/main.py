import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 12 : MATRIX Inverse ✅\n", "green")
    colorize_text("MATRIX\n", "purple")
    
    try:
        colorize_text("inverse of [[4.0, 7.0], [2.0, 6.0]]", "yellow")
        u0 = Matrix([
            [4.0, 7.0],
            [2.0, 6.0]
        ])
        print(f"{u0.inverse()}\nexpected :\n [[0.6, -0.7], [-0.2, 0.4]]]\n")
        
        colorize_text("inverse of [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]", "yellow")
        u1 = Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ])
        print(f"{u1.inverse()}\nexpected :\n[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]\n")
        
        colorize_text("inverse of [[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]]", "yellow")
        u2 = Matrix([
            [2.0, 0.0, 0.0],
            [0.0, 2.0, 0.0],
            [0.0, 0.0, 2.0]
        ])
        print(f"{u2.inverse()}\nexpected :\n[[0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]]\n")
        
        colorize_text("inverse of [[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]]", "yellow")
        u3 = Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0]
        ])
        print(f"{u3.inverse()}\nexpected :\n[[0.649425287, 0.097701149, -0.655172414], [-0.781609195, -0.126436782, 0.965517241], [0.143678161, 0.074712644, -0.206896552]]\n")

    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : \n", "red")
    try:
        colorize_text("inverse of [[2.0, 0.0, 0.0, 1.1],[0.0, 2.0, 0.0, 2.3],[0.0, 0.0, 2.0, 4.1]]", "yellow")
        u4 = Matrix([
            [2.0, 0.0, 0.0, 1.1],
            [0.0, 2.0, 0.0, 2.3],
            [0.0, 0.0, 2.0, 4.1]
        ])
        print(f"{u4.inverse()}\n")

    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : \n", "red")
    try:
        colorize_text("inverse of [[1.0, 2.0, 3.0],[2.0, 4.0, 6.0],[3.0, 6.0, 9.0]]", "yellow")
        u5 = Matrix([
            [1.0, 2.0, 3.0],
            [2.0, 4.0, 6.0],
            [3.0, 6.0, 9.0]
        ])
        print(f"{u5.inverse()}\n")

    except Exception as e:
        print(e)
        
    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")
    
    try:
        colorize_text("inverse of [[1, 0], [0, 1]]", "yellow")
        u6 = Matrix([[1, 0], [0, 1]])
        print(f"{u6.inverse()} \nexpected :\n[[1, 0], [0, 1]]\n")
        
        colorize_text("inverse of [[2, 0], [0, 2]]", "yellow")
        u7 = Matrix([[2, 0], [0, 2]])
        print(f"{u7.inverse()} \nexpected :\n[[0.5, 0], [0, 0.5]]\n")
        
        colorize_text("inverse of [[0.5, 0], [0, 0.5]]", "yellow")
        u8 = Matrix([[0.5, 0], [0, 0.5]])
        print(f"{u8.inverse()} \nexpected :\n[[2, 0], [0, 2]]\n")
        
        colorize_text("inverse of [[0, 1], [1, 0]]", "yellow")
        u9 = Matrix([[0, 1], [1, 0]])
        print(f"{u9.inverse()} \nexpected :\n[[0, 1], [1, 0]]\n")
        
        colorize_text("inverse of [[1, 2], [3, 4]]", "yellow")
        u10 = Matrix([[1, 2], [3, 4]])
        print(f"{u10.inverse()} \nexpected :\n[[-2, 1], [1.5, -0.5]]\n")
        
        colorize_text("inverse of [[1, 0, 0], [0, 1, 0], [0, 0, 1]]", "yellow")
        u11 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        print(f"{u11.inverse()} \nexpected :\n[[1, 0, 0], [0, 1, 0], [0, 0, 1]]\n")

    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
