import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from ex00.vector import Vector
from ex00.matrix import Matrix


def main():
    colorize_text("EXERCICE 04 : Norm\n", "green")
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

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
