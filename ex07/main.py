import sys
import os.path
# from matrix_mult import mul_vec
# from matrix_mult import mul_mat
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from ex00.vector import Vector
from ex00.matrix import Matrix


def main():
    colorize_text("EXERCICE 07 : MATRIX Multiplication\n", "green")
    colorize_text("MATRIX * VECTOR\n", "purple")

    try:
        u1 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v1 = Vector([4.0, 2.0])
        result1 = u1.mul_vec(v1)
        for row in result1.data:
            print(row)
        # [4.0]
        # [2.0]

        u2 = Matrix([[2.0, 0.0], [0.0, 2.0]])
        v2 = Vector([4.0, 2.0])
        result2 = u2.mul_vec(v2)
        for row in result2.data:
            print(row)
        # [8.0]
        # [4.0]

        u3 = Matrix([[2.0, -2.0], [-2.0, 2.0]])
        v3 = Vector([4.0, 2.0])
        result3 = u3.mul_vec(v3)
        for row in result3.data:
            print(row)
        # [4.0]
        # [-4.0]

        colorize_text("\nMATRIX * MATRIX\n", "purple")


        u4 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v4 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        result4 = u4.mul_mat(v4)
        for row in result4.data:
            print(row)
        # [1.0, 0.0]
        # [0.0, 1.0]

        u5 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v5 = Matrix([[2.0, 1.0], [4.0, 2.0]])
        result5 = u5.mul_mat(v5)
        for row in result5.data:
            print(row)
        # [2.0, 1.0]
        # [4.0, 2.0]

        u6 = Matrix([[3.0, -5.0], [6.0, 8.0]])
        v6 = Matrix([[2.0, 1.0], [4.0, 2.0]])
        result6 = u6.mul_mat(v6)
        for row in result6.data:
            print(row)
        # [-14, -7.0]
        # [44.0, 22.0]
        
        u7 = Matrix([[1.0, 4.0, -2.0], [3.0, 5.0, -6.0]])
        v7 = Matrix([[5.0, 2.0, 8.0, -1.0], [3.0, 6.0, 4.0, 5.0], [-2.0, 9.0, 7.0, -3.0]])
        result7 = u7.mul_mat(v7)
        for row in result7.data:
            print(row)
    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : ", "red")
    try:
        result7 = v7.mul_mat(u7)
        for row in result7.data:
                print(row)
    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
