#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

def make_lowercase(s):
    result = ""  #nitialize an empty string to store the result
    for char in s:  #LOop through each character in the input string
        if 'A' <= char <= 'Z':  #Check if the character is an uppercase letter
            result += chr(ord(char) + 32)  #convert to lowercase by adding 32 to ASCII value
        else:
            result += char  #if not uppercase, keep the character unchanged
    return result  #return the lowercase converted string

#Request input from user
user_input = input("Lagay ka po statement, sir: ")

#Applies custom function to user input
apply_function = make_lowercase(user_input) 


print(f"Formatted text: {apply_function}")  #Print the formatted text
