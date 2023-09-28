import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 04 : Norm ✅\n", "green")
    colorize_text("VECTOR\n", "purple")

    try:
        u1 = Vector([0.0, 0.0, 0.0])
        u2 = Vector([1.0, 2.0, 3.0])
        u3 = Vector([-1.0, -2.0])
    
        print("{}, {}, {}".format(u1.norm_1(), u1.norm(), u1.norm_inf()))  # 0.0, 0.0, 0.0
        print("{}, {}, {}".format(u2.norm_1(), u2.norm(), u2.norm_inf()))  # 6.0, 3.7416573867739413, 3.0
        print("{}, {}, {}".format(u3.norm_1(), u3.norm(), u3.norm_inf()))  # 3.0, 2.23606797749979, 2.0
    
    except Exception as e:
        print(e)

    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")

    try:
        colorize_text("Euclidian\n", "purple")
        
        v1 = Vector([0])
        result = v1.norm()
        print(f"{v1.data}.norm() gives {result} --> expected : 0")

        v2 = Vector([1])
        result = v2.norm()
        print(f"{v2.data}.norm() gives {result} --> expected : 1.0")

        v3 = Vector([0, 0])
        result = v3.norm()
        print(f"{v3.data}.norm() gives {result} --> expected : 0.0")

        v4 = Vector([1, 0])
        result = v4.norm()
        print(f"{v4.data}.norm() gives {result} --> expected : 1.0")

        v5 = Vector([2, 1])
        result = v5.norm()
        print(f"{v5.data}.norm() gives {result} --> expected : 2.236067977")

        v6 = Vector([4, 2])
        result = v6.norm()
        print(f"{v6.data}.norm() gives {result} --> expected : 4.472135955")

        v7 = Vector([-4, -2])
        result = v7.norm()
        print(f"{v7.data}.norm() gives {result} --> expected : 4.472135955")

        colorize_text("\nManhattan\n", "purple")

        v1 = Vector([0])
        result = v1.norm_1()
        print(f"{v1.data} returns {result} --> expected : 0")

        v2 = Vector([1])
        result = v2.norm_1()
        print(f"{v2.data} returns {result} --> expected : 1.0")

        v3 = Vector([0, 0])
        result = v3.norm_1()
        print(f"{v3.data} returns {result} --> expected : 0.0")

        v4 = Vector([1, 0])
        result = v4.norm_1()
        print(f"{v4.data} returns {result} --> expected : 1.0")

        v5 = Vector([2, 1])
        result = v5.norm_1()
        print(f"{v5.data} returns {result} --> expected : 3.0")

        v6 = Vector([4, 2])
        result = v6.norm_1()
        print(f"{v6.data} returns {result} --> expected : 6.0")

        v7 = Vector([-4, -2])
        result = v7.norm_1()
        print(f"{v7.data} returns {result} --> expected : 6.0")

    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
