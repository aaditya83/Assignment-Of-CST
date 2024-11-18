def get_positive_number():
    """
    Prompts the user to enter a positive number and validates the input using assertions.

    :return: A valid positive number.
    """
    number = float(input("Enter a positive number: "))
    # Assert that the input is positive
    assert number > 0, f"AssertionError: The input must be a positive number. Received: {number}"
    return number

# Example usage
if __name__ == "__main__":
    try:
        result = get_positive_number()
        print(f"Valid input received: {result}")
    except AssertionError as e:
        print(e)
