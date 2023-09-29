import sys
import os.path
from cross_product import cross_product
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 06 : Cross Product ✅\n", "green")
    colorize_text("VECTOR\n", "purple")

    try:
        colorize_text("cross product of [0.0, 0.0, 1.0] and [1.0, 0.0, 0.0]", "yellow")
        u1 = Vector([0.0, 0.0, 1.0])
        v1 = Vector([1.0, 0.0, 0.0])
        result1 = cross_product(u1, v1)
        print(f"{result1.data} --> expected : [0.0, 1.0, 0.0]\n")

        colorize_text("\ncross product of [1.0, 2.0, 3.0] and [4.0, 5.0, 6.0]", "yellow")
        u2 = Vector([1.0, 2.0, 3.0])
        v2 = Vector([4.0, 5.0, 6.0])
        result2 = cross_product(u2, v2)
        print(f"{result2.data} --> expected : [-3.0, 6.0, -3.0]\n")

        colorize_text("\ncross product of [4.0, 2.0, -3.0] and [-2.0, -5.0, 16.0]", "yellow")
        u3 = Vector([4.0, 2.0, -3.0])
        v3 = Vector([-2.0, -5.0, 16.0])
        result3 = cross_product(u3, v3)
        print(f"{result3.data} --> expected : [17.0, -58.0, -16.0]\n")

    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : ", "red")
    try:
        u4 = Vector([4.0, 2.0])
        v4 = Vector([-2.0, -5.0, 16.0])
        result3 = cross_product(u4, v4)

    except Exception as e:
        print(e)

    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")
    
    try:
        colorize_text("cross product of [0, 0, 0] and [0, 0, 0]", "yellow")
        u5 = Vector([0, 0, 0])
        v5 = Vector([0, 0, 0])
        print(f"{cross_product(u5, v5)} --> expected : [0, 0, 0]\n")
        
        colorize_text("cross product of [1, 0, 0] and [0, 0, 0]", "yellow")
        u6 = Vector([1, 0, 0])
        v6 = Vector([0, 0, 0])
        print(f"{cross_product(u6, v6)} --> expected : [0, 0, 0]\n")
        
        colorize_text("cross product of [1, 0, 0] and [0, 1, 0]", "yellow")
        u7 = Vector([1, 0, 0])
        v7 = Vector([0, 1, 0])
        print(f"{cross_product(u7, v7)} --> expected : [0, 0, 1]\n")
        
        colorize_text("cross product of [8, 7, -4] and [3, 2, 1]", "yellow")
        u8 = Vector([8, 7, -4])
        v8 = Vector([3, 2, 1])
        print(f"{cross_product(u8, v8)} --> expected : [15, -20, -5]\n")
        
        colorize_text("cross product of [1, 1, 1] and [0, 0, 0]", "yellow")
        u9 = Vector([1, 1, 1])
        v9 = Vector([0, 0, 0])
        print(f"{cross_product(u9, v9)} --> expected : [0, 0, 0]\n")
        
        colorize_text("cross product of [1, 1, 1] and [1, 1, 1]", "yellow")
        u10 = Vector([1, 1, 1])
        v10 = Vector([1, 1, 1])
        print(f"{cross_product(u10, v10)} --> expected : [0, 0, 0]\n")
    
    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
