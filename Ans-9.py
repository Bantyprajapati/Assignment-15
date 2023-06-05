# Write a python script to check if a string contains only characters of the alphabet.
def contains_only_alphabet(string):
    if string.isalpha():
        return True
    else:
        return False

# Example usage
string1 = "Hello"
result1 = contains_only_alphabet(string1)
print("String 1:", result1)

string2 = "Hello123"
result2 = contains_only_alphabet(string2)
print("String 2:", result2)
