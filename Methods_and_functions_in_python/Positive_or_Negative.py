def is_positive(number):
    """Function to check if a number is positive."""
    return number >= 0

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(is_positive(num))
    
    except ValueError:
        print("Please enter a valid interger.")
