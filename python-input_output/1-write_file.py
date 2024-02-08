#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written

# Example usage:
text = "Hello, world!"
filename = "output.txt"
num_chars_written = write_file(filename, text)
print(f"Number of characters written to {filename}: {num_chars_written}")
