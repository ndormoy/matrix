import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from ex00.vector import Vector
from ex00.matrix import Matrix


def main():
    colorize_text("EXERCICE 03\n", "green")
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

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
