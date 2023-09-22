from vector import Vector
from matrix import Matrix
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text



def main():
    colorize_text("EXERCICE 00\n", "green")
    colorize_text("VECTOR\n", "purple")
    
    try:
        # Vector addition, subtraction, and scaling tests
        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        u.add(v)
        print(u)
        # [7.0]
        # [10.0]

        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        u.sub(v)
        print(u)
        # [-3.0]
        # [-4.0]

        u = Vector([2.0, 3.0])
        u.scl(2.0)
        print(u)
        # [4.0]
        # [6.0]
    except ValueError as err:
        print(err)
    
    colorize_text("\nHas to fail : ", "red")
    try:
        w =  Vector([2.0, 3.0, 4.0])
        u.add(w)
    except ValueError as err:
        print(err)
        

    colorize_text("\n--------------------------------\n", "yellow")
    colorize_text("\nMATRIX\n", "purple")

    try:
        # Matrix addition, subtraction, and scaling tests
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        # u = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        u.add(v)
        print(u)
        # [8.0, 6.0]
        # [1.0, 6.0]

        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        u.sub(v)
        print(u)
        # [-6.0, -2.0]
        # [5.0, 2.0]

        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        u.scl(2.0)
        print(u)
        # [2.0, 4.0]
        # [6.0, 8.0]
    except ValueError as err:
        print(err)
        
    colorize_text("\nHas to fail : ", "red")
    try:
        w =  Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        u.add(w)
    except ValueError as err:
        print(err)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()