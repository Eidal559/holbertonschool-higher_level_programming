#!/usr/bin/python3
def uniq_add(my_list):
    # Use set to keep track of unique elements
    unique_set = set()

    # Iterate through the list and add unique elements to the set
    for num in my_list:
        unique_set.add(num)

    # Return the sum of unique elements
    return sum(unique_set)

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
  
