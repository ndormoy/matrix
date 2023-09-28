import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 03 : Dot Product ✅\n", "green")
    colorize_text("VECTOR\n", "purple")

    try:
        u = Vector([0.0, 0.0])
        v = Vector([1.0, 1.0])
        print(u.dot(v))  # 0.0

        u = Vector([1.0, 1.0])
        v = Vector([1.0, 1.0])
        print(u.dot(v))  # 2.0

        u = Vector([-1.0, 6.0])
        v = Vector([3.0, 2.0])
        print(u.dot(v))  # 9.0

    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : ", "red")
    try:
        u = Vector([0.0, 0.0])
        v = Vector([1.0, 1.0, 1.0])
        print(u.dot(v))
    except Exception as e:
        print(e)
        
    colorize_text("\nHas to fail : ", "red")
    try:
        u = Vector([0, 0])
        v = Vector([1.0, 1])
        print(u.dot(v))
    except Exception as e:
        print(e)

    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")

    try:
        v1 = Vector([0, 0])
        v2 = Vector([0, 0])
        result = v1.dot(v2)
        print(f"{v1.data} and {v2.data} gives {result} --> expected : 0")

        v1 = Vector([1, 0])
        v2 = Vector([0, 0])
        result = v1.dot(v2)
        print(f"{v1.data} and {v2.data} gives {result} --> expected : 0")

        v1 = Vector([1, 0])
        v2 = Vector([1, 0])
        result = v1.dot(v2)
        print(f"{v1.data} and {v2.data} gives {result} --> expected : 1")

        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        result = v1.dot(v2)
        print(f"{v1.data} and {v2.data} gives {result} --> expected : 0")

        v1 = Vector([1, 1])
        v2 = Vector([1, 1])
        result = v1.dot(v2)
        print(f"{v1.data} and {v2.data} gives {result} --> expected : 2")

        v1 = Vector([4, 2])
        v2 = Vector([2, 1])
        result = v1.dot(v2)
        print(f"{v1.data} and {v2.data} gives {result} --> expected : 10")

    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
