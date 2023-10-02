import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from utils.math import ft_abs
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 13 : MATRIX Rank ✅\n", "green")
    colorize_text("MATRIX\n", "purple")
    
    try:
        colorize_text("rank of [[1.0 0.0 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]\n", "yellow")
        u = Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ])
        print(f"rank = {u.rank()} --> expected : 3\n")

        colorize_text("rank of [[1.0, 2.0, 0.0, 0.0], [2.0, 4.0, 0.0, 0.0], [-1.0, 2.0, 1.0, 1.0]]\n", "yellow")
        u = Matrix([
            [1.0, 2.0, 0.0, 0.0],
            [2.0, 4.0, 0.0, 0.0],
            [-1.0, 2.0, 1.0, 1.0],
        ])
        print(f"rank = {u.rank()} --> expected : 2\n")

        colorize_text("rank of [[8.0, 5.0, -2.0],[4.0, 7.0, 20.0],[7.0, 6.0, 1.0],[21.0, 18.0, 7.0],]\n", "yellow")
        u = Matrix([
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0],
            [21.0, 18.0, 7.0],
        ])
        print(f"rank = {u.rank()} --> expected : 2\n")
        
    except Exception as e:
        print(e)


    colorize_text("\n--------------------------------\n", "purple")
    colorize_text("CORRECTION\n", "blue")
    
    try:
        colorize_text("rank of [[0, 0], [0, 0]]", "yellow")
        u = Matrix([[0, 0], [0, 0]])
        print(f"rank = {u.rank()} --> expected : 0\n")
        
        colorize_text("rank of [[1, 0], [0, 1]]", "yellow")
        u = Matrix([[1, 0], [0, 1]])
        print(f"rank = {u.rank()} --> expected : 1\n")
        
        colorize_text("rank of [[2, 0], [0, 2]]", "yellow")
        u = Matrix([[2, 0], [0, 2]])
        print(f"rank = {u.rank()} --> expected : 2\n")
        
        colorize_text("rank of [[1, 1], [1, 1]]", "yellow")
        u = Matrix([[1, 1], [1, 1]])
        print(f"rank = {u.rank()} --> expected : 1\n")
        
        colorize_text("rank of [[0, 1], [1, 0]]", "yellow")
        u = Matrix([[0, 1], [1, 0]])
        print(f"rank = {u.rank()} --> expected : 2\n")
        
        colorize_text("rank of [[1, 2], [3, 4]]", "yellow")
        u = Matrix([[1, 2], [3, 4]])
        print(f"rank = {u.rank()} --> expected : 2\n")
        
        colorize_text("rank of [[-7, 5], [4, 6]]", "yellow")
        u = Matrix([[-7, 5], [4, 6]])
        print(f"rank = {u.rank()} --> expected : 2\n")
        
        colorize_text("rank of [[1, 0, 0], [0, 1, 0], [0, 0, 1]]", "yellow")
        u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        print(f"rank = {u.rank()} --> expected : 3\n")
        
        
        
    except Exception as e:
        print(e)
    
    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
