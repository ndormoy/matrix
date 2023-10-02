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

    colorize_text("\n--------------------------------\n", "blue")
    colorize_text("CORRECTION\n", "blue")
    colorize_text("ADD\n", "purple")
    colorize_text("vector\n", "purple")
    colorize_text("'[0, 0]' and '[0, 0]", "yellow")
    u = Vector([0, 0])
    v = Vector([0, 0])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    colorize_text("'[1, 0]' and '[0, 1]", "yellow")
    u = Vector([1, 0])
    v = Vector([0, 1])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n[1, 1]\n")

    colorize_text("'[1, 1]' and '[1, 1]", "yellow")
    u = Vector([1, 1])
    v = Vector([1, 1])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n[2, 2]\n")

    colorize_text("'[21, 21]' and '[21, 21]", "yellow")
    u = Vector([21, 21])
    v = Vector([21, 21])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n[42, 42]\n")

    colorize_text("'[-21, 21]' and '[21, -21]", "yellow")
    u = Vector([-21, 21])
    v = Vector([21, -21])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    colorize_text("'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' and '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]", "yellow")
    u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n[9, 9, 9, 9, 9, 9, 9, 9, 9, 9]\n")

    colorize_text("\nmatrix\n", "purple")

    colorize_text("'[[0, 0], [0, 0]]' and '[[0, 0], [0, 0]]", "yellow")
    u = Matrix([[0, 0], [0, 0]])
    v = Matrix([[0, 0], [0, 0]])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n0 0\n0 0\n")

    colorize_text("'[[1, 0], [0, 1]]' and '[[0, 0], [0, 0]]", "yellow")
    u = Matrix([[1, 0], [0, 1]])
    v = Matrix([[0, 0], [0, 0]])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n1 0\n0 1\n")

    colorize_text("'[[1, 1], [1, 1]]' and '[[1, 1], [1, 1]]", "yellow")
    u = Matrix([[1, 1], [1, 1]])
    v = Matrix([[1, 1], [1, 1]])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n2 2\n2 2\n")

    colorize_text("'[[21, 21], [21, 21]]' and '[[21, 21], [21, 21]]", "yellow")
    u = Matrix([[21, 21], [21, 21]])
    v = Matrix([[21, 21], [21, 21]])
    u.add(v)
    print(f"Result : \n{u}\n\nExpected :\n42 42\n42 42\n")

    colorize_text("SUB\n", "purple")

    colorize_text("\nvector\n", "purple")

    colorize_text("'[0, 0]' sub '[0, 0]", "yellow")
    u = Vector([0, 0])
    v = Vector([0, 0])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    colorize_text("'[1, 0]' sub '[0, 1]", "yellow")
    u = Vector([1, 0])
    v = Vector([0, 1])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n[1, -1]\n")

    colorize_text("'[1, 1]' sub '[1, 1]", "yellow")
    u = Vector([1, 1])
    v = Vector([1, 1])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    colorize_text("'[21, 21]' sub '[21, 21]", "yellow")
    u = Vector([21, 21])
    v = Vector([21, 21])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n[0, 0]\n")

    colorize_text("'[-21, 21]' sub '[21, -21]", "yellow")
    u = Vector([-21, 21])
    v = Vector([21, -21])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n[-42, 42]\n")

    colorize_text("'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]' sub '[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]", "yellow")
    u = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    v = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n[-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]\n")

    colorize_text("\nMATRIX\n", "purple")

    colorize_text("'[[0, 0], [0, 0]]' sub '[[0, 0], [0, 0]]", "yellow")
    u = Matrix([[0, 0], [0, 0]])
    v = Matrix([[0, 0], [0, 0]])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n0 0\n0 0\n")

    colorize_text("'[[1, 0], [0, 1]]' sub '[[0, 0], [0, 0]]", "yellow")
    u = Matrix([[1, 0], [0, 1]])
    v = Matrix([[0, 0], [0, 0]])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n1 0\n0 1\n")

    colorize_text("'[[1, 1], [1, 1]]' sub '[[1, 1], [1, 1]]", "yellow")
    u = Matrix([[1, 1], [1, 1]])
    v = Matrix([[1, 1], [1, 1]])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n0 0\n0 0\n")

    colorize_text("'[[21, 21], [21, 21]]' sub '[[21, 21], [21, 21]]", "yellow")
    u = Matrix([[21, 21], [21, 21]])
    v = Matrix([[21, 21], [21, 21]])
    u.sub(v)
    print(f"Result : \n{u}\n\nExpected :\n0 0\n0 0\n")

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()