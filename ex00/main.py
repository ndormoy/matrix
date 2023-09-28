import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix
from utils.color import colorize_text
from utils.math import ft_abs



def main():
    colorize_text("EXERCICE 00 ✅\n", "green")
    colorize_text("VECTOR\n", "purple")
    
    try:
        # Vector addition, subtraction, and scaling tests
        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        u.add(v)
        print(f"{u}  --> expected : [7.0, 10.0]")

        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        u.sub(v)
        print(f"{u}  --> expected : [-3.0, -4.0]")

        u = Vector([2.0, 3.0])
        u.scl(2.0)
        print(f"{u}  --> expected : [4.0, 6.0]")

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
        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        u.add(v)
        print(f"Result : \n{u}\n\nExpected :\n8.0, 6.0\n1.0, 6.0\n")

        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        u.sub(v)
        print(f"Result : \n{u}\n\nExpected :\n-6.0, -2.0\n5.0, 2.0\n")

        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        u.scl(2.0)
        print(f"Result : \n{u}\n\nExpected :\n2.0, 4.0\n6.0, 8.0\n")

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