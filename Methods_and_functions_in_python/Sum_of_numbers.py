def sum_numbers(*args):
    """Function to sum a variable number of arguments."""
    sum_result = 0
    for number in args:
        sum_result += number
    return sum_result

if __name__ == "__main__":
    numbers = input("Enter numbers seperated by space: ").split()
    try:
        numbers = [int(num) for num in numbers]
        print(sum_numbers(*numbers))
    
    except ValueError:
        print("Please enter valid integers.")