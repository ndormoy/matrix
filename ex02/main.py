import sys
import os.path
from linear_interpolation import lerp
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from ex00.vector import Vector
from ex00.matrix import Matrix


def main():
    colorize_text("EXERCICE 02\n", "green")
    colorize_text("VECTOR\n", "purple")
    
    print(lerp(0.0, 1.0, 0.0)) # 0.0
    print(lerp(0.0, 1.0, 1)) # 1.0
    print(lerp(0.0, 1.0, 0.5)) # 0.5
    print(lerp(21.0, 42.0, 0.3)) # 27.3
    
    try:
        
        print(lerp(Vector([2.0, 1.0]), Vector([4., 2.]), 0.3)) # [2.6, 1.3]
        # print(lerp(Vector([1.0, 2.0, 3.0]), Vector([14.0, 25.0, 6.0]), 1)) # [2.6, 1.3]
        
        
        print(lerp(Matrix([[2.0, 1.0], [3.0, 4.0]]), Matrix([[20.0, 10.0], [30.0, 40.0]]), 0.5)) # [[11.0, 5.5], [16.5, 22.0]]
        
    except Exception as e:
        print(e)
    # colorize_text("\nHas to fail : ", "red")


    # colorize_text("\n--------------------------------\n", "yellow")
    # colorize_text("\nMATRIX\n", "purple")


        
    # colorize_text("\nHas to fail : ", "red")


    # colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
