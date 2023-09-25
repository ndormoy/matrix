import sys
import os.path
from cross_product import cross_product
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from ex00.vector import Vector
from ex00.matrix import Matrix


def main():
    colorize_text("EXERCICE 06 : Cross Product\n", "green")
    colorize_text("VECTOR\n", "purple")

    try:
        u1 = Vector([0.0, 0.0, 1.0])
        v1 = Vector([1.0, 0.0, 0.0])
        result1 = cross_product(u1, v1)
        print(result1.data)  # [0.0, 1.0, 0.0]

        u2 = Vector([1.0, 2.0, 3.0])
        v2 = Vector([4.0, 5.0, 6.0])
        result2 = cross_product(u2, v2)
        print(result2.data)  # [-3.0, 6.0, -3.0]

        u3 = Vector([4.0, 2.0, -3.0])
        v3 = Vector([-2.0, -5.0, 16.0])
        result3 = cross_product(u3, v3)
        print(result3.data)  # [17.0, -58.0, -16.0]

    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : ", "red")
    try:
        u4 = Vector([4.0, 2.0])
        v4 = Vector([-2.0, -5.0, 16.0])
        result3 = cross_product(u4, v4)

    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
