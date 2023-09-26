import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 13 : MATRIX Rank ✅\n", "green")
    colorize_text("MATRIX\n", "purple")
    
    try:
        u = Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ])
        print(f"rank = {u.rank()}\n")
        # Output: 3

        # Create a new matrix u
        u = Matrix([
            [1.0, 2.0, 0.0, 0.0],
            [2.0, 4.0, 0.0, 0.0],
            [-1.0, 2.0, 1.0, 1.0],
        ])
        print(f"rank = {u.rank()}\n")
        # Output: 2

        # Create another matrix u
        u = Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0],
            [21.0, 18.0, 7.0],
        ])
        print(f"rank = {u.rank()}\n")
        # Output: 3
        
    except Exception as e:
        print(e)


    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
