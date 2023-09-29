import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 09 : MATRIX Transpose ✅\n", "green")
    colorize_text("MATRIX\n", "purple")

    try:
        colorize_text("transpose of [[1.0, 2.0], [3.0, 4.0]]", "yellow")
        u1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        print(f"BEFORE : \n{u1}\n")
        print(f"AFTER \n{u1.transpose()}\n")

        colorize_text("transpose of [[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]]", "yellow")
        u2 = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
        print(f"BEFORE : \n{u2}\n")
        print(f"AFTER \n{u2.transpose()}\n")

        colorize_text("transpose of [1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]]", "yellow")
        u3 = Matrix([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]])
        print(f"BEFORE : \n{u3}\n")
        print(f"AFTER \n{u3.transpose()}\n")

    except Exception as e:
        print(e)
        
    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")
    
    try:
        colorize_text("transpose of [[0, 0], [0, 0]]", "yellow")
        u4 = Matrix([[0, 0], [0, 0]])
        print(f"{u4.transpose()} \nexpected :\n[[0, 0], [0, 0]]")
    
        colorize_text("transpose of [[1, 0], [0, 0]]", "yellow")
        u5 = Matrix([[1, 0], [0, 1]])
        print(f"{u5.transpose()} \nexpected :\n[[1, 0], [0, 1]]")
        
        colorize_text("transpose of [[1, 2], [3, 4]]", "yellow")
        u6 = Matrix([[1, 2], [3, 4]])
        print(f"{u6.transpose()} \nexpected :\n[[1, 3], [2, 4]]")
        
        colorize_text("transpose of [[1, 0, 0], [0, 1, 0], [0, 0, 1]]", "yellow")
        u7 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        print(f"{u7.transpose()} \nexpected :\n[[1, 0, 0], [0, 1, 0], [0, 0, 1]]")
    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
