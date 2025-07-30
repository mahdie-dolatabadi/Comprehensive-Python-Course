def is_even(number):
    """Function to check if a number is even."""
    return number % 2 == 0


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(is_even(num))
    except ValueError:
        print("Please enter a valid number.")