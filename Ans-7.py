# Write a python script to determine whether a string contains a specific substring.
def contains_substring(string, substring):
    if substring in string:
        return True
    else:
        return False

# Example usage
string = "Hello, World!"
substring = "World"
result = contains_substring(string, substring)
print("Result:", result)
