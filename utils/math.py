def ft_abs(number):
    if number < 0:
        return -number
    return number

def ft_max(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    
    return maximum