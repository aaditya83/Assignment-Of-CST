# Function to sort a list of dictionaries by a specified key
def sort_dict_list(dict_list, key):
    """
    Sorts a list of dictionaries by the specified key.

    :param dict_list: List of dictionaries to be sorted.
    :param key: The key in each dictionary by which to sort.
    :return: A sorted list of dictionaries.
    """
    try:
        return sorted(dict_list, key=lambda x: x[key])
    except KeyError:
        print(f"Error: One or more dictionaries do not have the key '{key}'.")
        return []
    except TypeError:
        print("Error: The list contains non-dictionary elements.")
        return []

# Example usage
if __name__ == "__main__":
    # Example list of dictionaries
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "David", "age": 28}
    ]

    print("Original list:")
    for person in people:
        print(person)

    # Sort the list of dictionaries by 'age'
    sorted_people = sort_dict_list(people, "age")

    print("\nSorted by age:")
    for person in sorted_people:
        print(person)

    # Sort the list of dictionaries by 'name'
    sorted_people_by_name = sort_dict_list(people, "name")

    print("\nSorted by name:")
    for person in sorted_people_by_name:
        print(person)
