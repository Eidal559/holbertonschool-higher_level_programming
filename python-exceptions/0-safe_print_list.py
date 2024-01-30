#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            pass
        except IndexError:
            break
        else:
            print("{}".format(my_list[i]), end="")
            total += 1
    print()
    return total
