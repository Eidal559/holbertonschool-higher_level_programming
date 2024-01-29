#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Update or add the key-value pair in the dictionary
    a_dictionary[key] = value
    return a_dictionary

# Example usage:
if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}

    # Update 'language' key
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    # Add 'city' key
    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)
