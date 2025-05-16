def calculate_average(numbers):

    #BBBBRRRR
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    average = sum / len(numbers)
    return average

def unsafe_division(a, b):
    return a / b

def unused_function():
    pass

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Average:", calculate_average(nums))
    print("Division:", unsafe_division(10, 0))