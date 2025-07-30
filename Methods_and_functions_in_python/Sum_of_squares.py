def sum_of_squares(number0, number1):
    """Function to calculate the sum of squares of two numbers."""
    return number0**2 + number1**2

if __name__ == "__main__":
    try:
        num0 = int(input("Enter the first number: "))
        num1 = int(input("Enter the second number: "))
        print(sum_of_squares(num0, num1))

    except ValueError:
        print("Please enter valid integers.")