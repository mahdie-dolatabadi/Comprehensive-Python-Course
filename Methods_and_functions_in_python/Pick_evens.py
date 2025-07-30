def pick_evens(*args):
    """
    This function takes any number of arguments and returns a list of even numbers.
    """
    evens = [num for num in args if num % 2 == 0]
    return evens

if __name__ == "__main__":
    numbers = input("Enter numbers seperated by soace: ").split()
    try:
        numbers = [int(num) for num in numbers]
        print(pick_evens(*numbers))

    except ValueError:
        print("Please enter valid integers.")