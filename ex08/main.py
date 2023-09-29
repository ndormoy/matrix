import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 08 : MATRIX Trace ✅\n", "green")
    colorize_text("MATRIX\n", "purple")

    try:
        colorize_text("trace of [[1.0, 0.0], [0.0, 1.0]]", "yellow")
        u1 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        print(u1.trace())  # Output: 2.0

        colorize_text("trace of [[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]]", "yellow")
        u2 = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
        print(u2.trace())  # Output: 9.0

        colorize_text("trace of [[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]]", "yellow")
        u3 = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]])
        print(u3.trace())  # Output: -21.0

    except Exception as e:
        print(e)
        
    colorize_text("\nHas to fail : ", "red")
    try:
        colorize_text("trace of [[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0], [4.0, 2.0, 9.0]]", "yellow")
        u4 = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0], [4.0, 2.0, 9.0]])
        print(u4.trace())
        
       
    except Exception as e:
        print(e)
        
    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")
    
    try:
        colorize_text("trace of [[0, 0], [0, 0]]", "yellow")
        u5 = Matrix([[0, 0], [0, 0]])
        print(f"{u5.trace()} --> expected : 0\n")  # Output: 0
        
        colorize_text("trace of [[1, 0], [0, 0]]", "yellow")
        u6 = Matrix([[1, 0], [0, 1]])
        print(f"{u6.trace()} --> expected : 2\n")  # Output: 2
        
        colorize_text("trace of [[1, 2], [3, 4]]", "yellow")
        u7 = Matrix([[1, 2], [3, 4]])
        print(f"{u7.trace()} --> expected : 5\n")  # Output: 5
        
        colorize_text("trace of [[8, -7], [4, 2]]", "yellow")
        u8 = Matrix([[8, -7], [4, 2]])
        print(f"{u8.trace()} --> expected : 10\n")  # Output: 10
        
        colorize_text("trace of [[1, 0, 0], [0, 1, 0], [0, 0, 1]]", "yellow")
        u9 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        print(f"{u9.trace()} --> expected : 3\n")  # Output: 3
    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
