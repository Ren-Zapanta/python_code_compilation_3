#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
def remove_leading_spaces(text): #defines a function
    for i, char in enumerate(text): #goes through each character in the text
        if char != ' ': #Validates non-space character
            return text[i:] #returns that string from that position
        
    return ""

input_text = "   Hello sir, Danilo"
print(f"Original text: {repr(input_text)}") #Original text
print(f"Formatted text: {repr(remove_leading_spaces(input_text))}") #Formatted text




