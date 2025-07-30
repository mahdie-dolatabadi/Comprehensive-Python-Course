def skyline(*args):
    """
    This function takes any number of arguments representing building heights
    and returns the height of the tallest building.
    """
    if not args:
        return 0
    return max(args)

if __name__ == "__main__":
    heights = input("Enter the heights of buildings seperated by space: ").split()
    try:
        heights = [int(height) for height in heights]
        print(skyline(*heights))
        
    except ValueError:
        print("Please enter valid integers.")
