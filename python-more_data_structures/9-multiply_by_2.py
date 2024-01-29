#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Use a dictionary comprehension to multiply each value by 2
    return {key: value * 2 for key, value in a_dictionary.items()}

# Example usage:
if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
