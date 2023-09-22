import os
import sys
import time



"""
    Run all of the exercises.
"""


def waiting_bar(iterations, delay=0.01):
    sys.stdout.write("loading [...]")

    for i in range(iterations + 1):
        sys.stdout.write('\r')
        sys.stdout.write(f"[{'=' * i}{' ' * (iterations - i)}] {i}/{iterations}")
        sys.stdout.flush()
        time.sleep(delay)

    # Clear the loading message
    sys.stdout.write('\r\033[K')  # ANSI escape code to clear the line
    sys.stdout.flush()

def main():
    sys.stdout.write("loading [...]")
    sys.stdout.flush()
    num_iterations = 50
    time.sleep(0.5)
    waiting_bar(num_iterations)
    for i in range(2):
        os.system(f"python3 ex0{i}/main.py")

if __name__ == '__main__':
    main()
    