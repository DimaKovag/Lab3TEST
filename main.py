def calculate_average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)

def safe_division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Average:", calculate_average(nums))
    try:
        print("Division:", safe_division(10, 2))
    except ValueError as e:
        print(e)