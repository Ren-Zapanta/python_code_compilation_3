#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
user_input = input("Please enter a statement: ") #Requests input from user

formatted_text = "" #Creates an empty string for the result

for char in user_input: #loops through the characters
    if char.islower(): #converts lowercase to upper case
        formatted_text += char.upper()
    elif char.isupper(): #converts uppercase to lower case
        formatted_text += char.lower()  
    else: 
        formatted_text += char #adds characters back without converting

print(formatted_text) #Prints result
        

