import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 12 : MATRIX Inverse ✅\n", "green")
    colorize_text("MATRIX\n", "purple")
    
    try:
        u0 = Matrix([
            [4.0, 7.0],
            [2.0, 6.0]
        ])
        print(f"{u0.inverse()}\n")
        # [0.6, -0.7]
        # [-0.2, 0.4]
        
        u1 = Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ])
        print(f"{u1.inverse()}\n")
        # [1.0, 0.0, 0.0]
        # [0.0, 1.0, 0.0]
        # [0.0, 0.0, 1.0]
        u2 = Matrix([
            [2.0, 0.0, 0.0],
            [0.0, 2.0, 0.0],
            [0.0, 0.0, 2.0]
        ])
        print(f"{u2.inverse()}\n")
        # [0.5, 0.0, 0.0]
        # [0.0, 0.5, 0.0]
        # [0.0, 0.0, 0.5]
        u3 = Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0]
        ])
        print(f"{u3.inverse()}\n")
        # # [0.649425287, 0.097701149, -0.655172414]
        # # [-0.781609195, -0.126436782, 0.965517241]
        # [0.143678161, 0.074712644, -0.206896552]

    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : \n", "red")
    try:
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
        u5 = Matrix([
            [1.0, 2.0, 3.0],
            [2.0, 4.0, 6.0],
            [3.0, 6.0, 9.0]
        ])
        print(f"{u5.inverse()}\n")

    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
