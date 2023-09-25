import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 08 : MATRIX Trace\n", "green")
    colorize_text("MATRIX\n", "purple")

    try:
        u1 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        print(u1.trace())  # Output: 2.0

        u2 = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
        print(u2.trace())  # Output: 9.0

        u3 = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]])
        print(u3.trace())  # Output: -21.0

    except Exception as e:
        print(e)
        
    colorize_text("\nHas to fail : ", "red")
    try:
        u4 = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0], [4.0, 2.0, 9.0]])
        print(u4.trace())
        
       
    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
