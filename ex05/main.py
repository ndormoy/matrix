import sys
import os.path
from angle_cos import angle_cos
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 05 : Cosine\n", "green")
    colorize_text("VECTOR\n", "purple")

    try:
        u1 = Vector([1.0, 0.0])
        v1 = Vector([1.0, 0.0])
        print("{}".format(angle_cos(u1, v1)))  # 1.0

        u2 = Vector([1.0, 0.0])
        v2 = Vector([0.0, 1.0])
        print("{}".format(angle_cos(u2, v2)))  # 0.0

        u3 = Vector([-1.0, 1.0])
        v3 = Vector([1.0, -1.0])
        print("{}".format(angle_cos(u3, v3)))  # -1.0

        u4 = Vector([2.0, 1.0])
        v4 = Vector([4.0, 2.0])
        print("{}".format(angle_cos(u4, v4)))  # 1.0

        u5 = Vector([1.0, 2.0, 3.0])
        v5 = Vector([4.0, 5.0, 6.0])
        print("{}".format(angle_cos(u5, v5)))  # 0.974631846

    except Exception as e:
        print(e)

    colorize_text("\nUndefined : ", "red")
    try:
        u = Vector([0.0, 0.0])
        v = Vector([1.0, 1.0, 1.0])
        print("{}".format(angle_cos(u, v)))  # 1.0
    except Exception as e:
        print(e)

    colorize_text("\nUndefined : ", "red")
    try:
        u = Vector([0.0, 0.0])
        v = Vector([0.0, 0.0])

        print("{}".format(angle_cos(u, v)))  # 1.0
    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
