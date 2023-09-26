import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from utils.color import colorize_text
from vector_matrix.vector import Vector
from vector_matrix.matrix import Matrix


def main():
    colorize_text("EXERCICE 13 : MATRIX Rank\n", "green")
    colorize_text("MATRIX\n", "purple")
    
    try:
        pass
        
    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : \n", "red")
    try:
        pass

    except Exception as e:
        print(e)

    colorize_text("\nHas to fail : ", "red")
    try:
        pass

    except Exception as e:
        print(e)

    colorize_text("\n================================\n", "cyan")

if __name__ == '__main__':
    main()
