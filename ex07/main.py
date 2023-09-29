import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 07 : MATRIX Multiplication ✅\n", "green")
    colorize_text("MATRIX * VECTOR\n", "purple")

    try:
        colorize_text("linear transformation of [[1.0, 0.0], [0.0, 1.0]] and vector [4.0, 2.0]", "yellow")
        u1 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v1 = Vector([4.0, 2.0])
        result1 = u1.mul_vec(v1)
        for row in result1.data:
            print(row)
        # [4.0]
        # [2.0]
        print("\n")

        colorize_text("linear transformation of [[2.0, 0.0], [0.0, 2.0]] and vector [4.0, 2.0]", "yellow")
        u2 = Matrix([[2.0, 0.0], [0.0, 2.0]])
        v2 = Vector([4.0, 2.0])
        result2 = u2.mul_vec(v2)
        for row in result2.data:
            print(row)
        # [8.0]
        # [4.0]
        print("\n")

        colorize_text("linear transformation of [[0.5, 0.0], [0.0, 0.5]] and vector [4.0, 2.0]", "yellow")
        u3 = Matrix([[2.0, -2.0], [-2.0, 2.0]])
        v3 = Vector([4.0, 2.0])
        result3 = u3.mul_vec(v3)
        for row in result3.data:
            print(row)
        # [4.0]
        # [-4.0]

        colorize_text("\nMATRIX * MATRIX\n", "purple")

        colorize_text("linear transformation of [[1.0, 0.0], [0.0, 1.0]] and [[1.0, 0.0], [0.0, 1.0]]", "yellow")
        u4 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v4 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        result4 = u4.mul_mat(v4)
        for row in result4.data:
            print(row)
        # [1.0, 0.0]
        # [0.0, 1.0]
        print("\n")

        colorize_text("linear transformation of [[1.0, 0.0], [0.0, 1.0]] and [[2.0, 1.0], [4.0, 2.0]]", "yellow")
        u5 = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v5 = Matrix([[2.0, 1.0], [4.0, 2.0]])
        result5 = u5.mul_mat(v5)
        for row in result5.data:
            print(row)
        # [2.0, 1.0]
        # [4.0, 2.0]
        print("\n")

        colorize_text("linear transformation of [[3.0, -5.0], [6.0, 8.0]] and [[2.0, 1.0], [4.0, 2.0]]", "yellow")
        u6 = Matrix([[3.0, -5.0], [6.0, 8.0]])
        v6 = Matrix([[2.0, 1.0], [4.0, 2.0]])
        result6 = u6.mul_mat(v6)
        for row in result6.data:
            print(row)
        # [-14, -7.0]
        # [44.0, 22.0]
        print("\n")

        colorize_text("linear transformation of [[1.0, 4.0, -2.0], [3.0, 5.0, -6.0]] and [[5.0, 2.0, 8.0, -1.0], [3.0, 6.0, 4.0, 5.0], [-2.0, 9.0, 7.0, -3.0]]", "yellow")
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
        
    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")
    
    try:
        colorize_text("linear transformation of [[0, 0], [0, 0]] and any vector dimension 2 will only return vector with only zero in it", "yellow")
        u8 = Matrix([[0, 0], [0, 0]])
        v8 = Vector([3, 7])
        print(f"{u8.mul_vec(v8)} --> expected [0, 0]\n")
        
        colorize_text("linear transformation of [[1, 0], [0, 1]] and any vector dimension 2 will return the same vector as given it", "yellow")
        u9 = Matrix([[1, 0], [0, 1]])
        v9 = Vector([3, 7])
        print(f"{u9.mul_vec(v9)} --> expected [3, 7]\n")
        
        colorize_text("linear transformation of [[1, 0], [0, 1]] and vector [4, 2]", "yellow")
        u10 = Matrix([[1, 1], [1, 1]])
        v10 = Vector([4, 2])
        print(f"{u10.mul_vec(v10)} --> expected [6, 6]\n")
        
        colorize_text("linear transformation of [[2, 0], [0, 2]] and vector [2, 1]", "yellow")
        u11 = Matrix([[2, 0], [0, 2]])
        v11 = Vector([2, 1])
        print(f"{u11.mul_vec(v11)} --> expected [4, 2]\n")
        
        colorize_text("linear transformation of [[0.5, 0], [0, 0.5]] and vector [4, 2]", "yellow")
        u12 = Matrix([[0.5, 0], [0, 0.5]])
        v12 = Vector([4, 2])
        print(f"{u12.mul_vec(v12)} --> expected [2, 1]\n")
        
        
    except Exception as e:
        print(e)
        
    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
