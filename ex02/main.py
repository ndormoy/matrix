import sys
import os.path
from linear_interpolation import lerp
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix




def main():
    colorize_text("EXERCICE 02 : Linear interpolation ✅\n", "green")
    colorize_text("NUMBERS\n", "purple")
    try:
        print(f"{lerp(0.0, 1.0, 0.0)} --> expected : 0.0")
        print(f"{lerp(0.0, 1.0, 1)} --> expected : 1.0")
        print(f"{lerp(0.0, 1.0, 0.5)} --> expected : 0.5")
        print(f"{lerp(21.0, 42.0, 0.3)} --> expected : 27.3")

    except Exception as e:
        print(e)
    
    colorize_text("\nHas to fail : ", "red")
    
    try:
        print(lerp(0.0, 1.0, -0.1))
    except Exception as e:
        print(e)
        
    colorize_text("\n--------------------------------\n", "yellow")


    colorize_text("\nVECTOR AND MATRIX\n", "purple")

    try:
        
        print(f"result:\n{lerp(Vector([2.0, 1.0]), Vector([4.0, 2.0]), 0.3)}\nexpected :\n[2.6, 1.3]\n")
        print(f"result:\n{lerp(Matrix([[2.0, 1.0], [3.0, 4.0]]), Matrix([[20.0, 10.0], [30.0, 40.0]]), 0.5)}\nexpected :\n[[11.0, 5.5], [16.5, 22.0]]\n")

    except Exception as e:
        print(e)

        
    colorize_text("\nHas to fail : ", "red")
    try:
        print(lerp(Vector([2.0, 1.0, 4.0]), Vector([4.0, 2.0]), 0.8))
    except Exception as e:
        print(e)
    try:
        print(lerp(Vector([2.0, 1.0, 4.0]), Matrix([[20.0, 10.0], [30.0, 40.0]]), 0.8))
    except Exception as e:
        print(e)
    try:
        print(lerp(Matrix([[2.0, 1.0], [3.0, 4.0]]), Matrix([[20.0, 10.0, 13.0], [30.0, 40.0, 50.0]]), 0.7))
    except Exception as e:
        print(e)

    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")

    try:
        colorize_text("lerp(0., 1., 0.)", "yellow")
        print(f"{lerp(0., 1., 0.)} --> expected : 0.0\n")

        colorize_text("lerp(0., 1., 1.)", "yellow")
        print(f"{lerp(0., 1., 1.)} --> expected : 1.0\n")

        colorize_text("lerp(0., 42., 0.5)", "yellow")
        print(f"{lerp(0., 42., 0.5)} --> expected : 21.0\n")

        colorize_text("lerp(-42., 42., 0.5)", "yellow")
        print(f"{lerp(-42., 42., 0.5)} --> expected : 0.0\n")

        colorize_text("lerp(Vector([-42, 42]), Vector([42, -42]), 0.5)", "yellow")
        print(f"{lerp(Vector([-42, 42]), Vector([42, -42]), 0.5)} --> expected : [0.0, 0.0]\n")

    except Exception as e:
        print(e)


    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
