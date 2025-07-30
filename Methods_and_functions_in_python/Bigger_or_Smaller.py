def is_greater(number0, number1):
    """Function to compare two numbers and return if the first is greater than the second."""
    return number0 > number1

if __name__ == "__main__":
    try:
        num0 = int(input("Enter the first number: "))
        num1 = int(input("Enter the second number: "))
        print(is_greater(num0, num1))
    
    except ValueError:
        print("Please enter a valid integer.")