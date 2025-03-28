#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
def custom_removeprefix(string, prefix):
    # Check if the string starts with the given prefix
    if string.startswith(prefix):  # If the prefix is found at the beginning
        return string[len(prefix):]  # Remove the prefix by slicing the string
    return string  # If no prefix match, return the original string

original_string = "Ungrateful sa grades" #Originial String
prefix_to_remove = "Un" #Specified prefix


formatted_string = custom_removeprefix(original_string, prefix_to_remove) #Calls the custom function

# Display the result
print(f"Original string: {original_string}")  # Print the original string
print(f"Formatted string: {formatted_string}")  # Print the modified string without the prefix
