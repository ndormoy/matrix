import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix
from linear_combination import linear_combination
from utils.math import ft_abs



def main():
    colorize_text("EXERCICE 01 : Linear combination ✅\n", "green")
    colorize_text("VECTOR\n", "purple")
    
    try:
        # Define vectors
        e1 = Vector([1.0, 0.0, 0.0])
        e2 = Vector([0.0, 1.0, 0.0])
        e3 = Vector([0.0, 0.0, 1.0])
        v1 = Vector([1.0, 2.0, 3.0])
        v2 = Vector([0.0, 10.0, -100.0])

        # Define coefficients
        coefficients1 = [10.0, -2.0, 0.5]
        coefficients2 = [10.0, -2.0]

        # Perform linear combinations
        result1 = linear_combination([e1, e2, e3], coefficients1) # [10, -2, 0.5]
        # result1[0] = 10 * e1[0] - 2 * e2[0] + 0.5 * e3[0] = 10 * 1 - 2 * 0 + 0.5 * 0 = 10.0
        # result1[1] = 10 * e1[1] - 2 * e2[1] + 0.5 * e3[1] = 10 * 0 - 2 * 1 + 0.5 * 0 = -2.0
        # result1[2] = 10 * e1[2] - 2 * e2[2] + 0.5 * e3[2] = 10 * 0 - 2 * 0 + 0.5 * 1 = 0.5
        result2 = linear_combination([v1, v2], coefficients2) # [10, 0, 230.0]
        # result2[0] = 10 * v1[0] -2 * v2[0] = 10 * 1 -2 * 0 = 10
        # result2[1] = 10 * v1[1] -2 * v2[1] = 10 * 2 -2 * 10 = 0
        # result2[2] = 10 * v1[2] -2 * v2[2] = 10 * 3 -2 * -100 = 230

        # Print results
        print(f"{result1} --> expected : [10.0, -2.0, 0.5]")
        
        print(f"{result2} --> expected : [10.0, 0.0, 230.0]")
    except ValueError as e:
        print(e)
    
    colorize_text("\nHas to fail : ", "red")
    try:
        v3 = Vector([1.0, 2.0, 3.0, 4.0])
        result3 = linear_combination([v1, v3], coefficients2)
        print(result3)
    except ValueError as e:
        print(e)

    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")
    try:
        colorize_text("linear_combination([Vector([-42, 42])], [-1.])", "yellow")
        result0 = linear_combination([Vector([-42, 42])], [-1.])
        print(f"{result0} --> expected : [42.0, -42.0]\n")

        colorize_text("linear_combination([Vector([-42.]), Vector([-42.]), Vector([-42.])], [-1., 1., 0.])", "yellow")
        result1 = linear_combination([Vector([-42.]), Vector([-42.]), Vector([-42.])], [-1., 1., 0.])
        print(f"{result1} --> expected : [0.0]\n")

        colorize_text("linear_combination([Vector([-42., 42.]), Vector([1., 3.]), Vector([10., 20.])], [1., -10., -1.])", "yellow")
        result2 = linear_combination([Vector([-42., 42.]), Vector([1., 3.]), Vector([10., 20.])], [1., -10., -1.])
        print(f"{result2} --> expected : [-62.0, -8.0]\n")

        colorize_text("linear_combination([Vector([-42., 100., -69.5]), Vector([1., 3., 5.])], [1., -10.])", "yellow")
        result3 = linear_combination([Vector([-42., 100., -69.5]), Vector([1., 3., 5.])], [1., -10.])
        print(f"{result3} --> expected : [-52.0, 70.0, -119.5]\n")

        print(f"")
    except ValueError as e:
        print(e)


    
    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()