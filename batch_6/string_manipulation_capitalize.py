#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
user_input = input("Please enter a statement: ") #Asks the user for an input

if user_input: #Converts the corresponding index to the approriate casing using lower and upper functions
    formatted_text = user_input[0].upper() + user_input[1:].lower()
else:
    formatted_text = "" #Returns empty if empty

print(formatted_text) #Prints result
