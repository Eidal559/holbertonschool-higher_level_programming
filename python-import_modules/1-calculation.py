#!/usr/bin/python3
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

a = 10
b = 5

from calculator_1 import add, subtract, multiply, divide

result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

print("Addition: {} + {} = {}".format(a, b, result_add))
print("Subtraction: {} - {} = {}".format(a, b, result_subtract))
print("Multiplication: {} * {} = {}".format(a, b, result_multiply))
print("Division: {} / {} = {}".format(a, b, result_divide))
