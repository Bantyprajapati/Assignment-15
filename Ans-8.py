# Write a python script to check if a string contains only numbers.
def contains_only_numbers(string):
    if string.isdigit():
        return True
    else:
        return False

# Example usage
string1 = "12345"
result1 = contains_only_numbers(string1)
print("String 1:", result1)

string2 = "123abc"
result2 = contains_only_numbers(string2)
print("String 2:", result2)
