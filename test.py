import numpy as np

def main():
    revenue = np.array([[200, 220, 250], [68, 79, 105], [110, 140, 180], [80, 85, 90]])
    print(75 * revenue)
    
    flower_sold = np.array([[50, 60, 25], [10, 13, 5], [40, 70, 52]])
    flower_unit = np.array([20, 30, 15])
    # print(flower_sold * flower_unit)
    res = np.dot(flower_unit, flower_sold)
    print(res)
if __name__ == '__main__':
    main()