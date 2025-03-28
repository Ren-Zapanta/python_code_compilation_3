#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
def custom_removeprefix(string, prefix):
    # Check if the string starts with the given prefix
    if string.startswith(prefix):  # If the prefix is found at the beginning
        return string[len(prefix):]  # Remove the prefix by slicing the string
    return string  # If no prefix match, return the original string