#!/usr/bin/python3
def multiply_list_map(my_list, multiplier):
    # Use map() to apply the multiplication to each element in the list
    return list(map(lambda x: x * multiplier, my_list))

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)
