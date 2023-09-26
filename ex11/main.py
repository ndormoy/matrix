import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 11 : MATRIX Determinant ✅\n", "green")
    colorize_text("MATRIX\n", "purple")
    
    try:
        # Matrix u1
        u1_data = [
            [1.0, -1.0],
            [-1.0, 1.0],
        ]
        u1 = Matrix(u1_data)
        print(f"{u1.determinant()}")
        # 0.0

        # Matrix u2
        u2_data = [
            [2.0, 0.0, 0.0],
            [0.0, 2.0, 0.0],
            [0.0, 0.0, 2.0],
        ]
        u2 = Matrix(u2_data)
        print(f"{u2.determinant()}")
        # 8.0

        # Matrix u3
        u3_data = [
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0],
        ]
        u3 = Matrix(u3_data)
        print(f"{u3.determinant()}")
        # -174.0

        # Matrix u4
        u4_data = [
            [8.0, 5.0, -2.0, 4.0],
            [4.0, 2.5, 20.0, 4.0],
            [8.0, 5.0, 1.0, 4.0],
            [28.0, -4.0, 17.0, 1.0],
        ]
        u4 = Matrix(u4_data)
        print(f"{u4.determinant()}")
        # 1032.0
        
    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : \n", "red")
    try:
        u5_data = [
            [8.0, 5.0, -2.0, 4.0],
            [4.0, 2.5, 20.0, 4.0],
            [8.0, 5.0, 1.0, 4.0],
            [28.0, -4.0, 17.0, 1.0],
            [25.0, -2.0, 1.0, 16.0],
        ]
        u5 = Matrix(u5_data)
        print(f"{u5.determinant()}")

    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : ", "red")
    try:
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

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
