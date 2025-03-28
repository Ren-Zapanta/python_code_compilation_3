#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
def verify_uppercase(s): #Creates custom function
    for char in s: #loops through each character in the given string
        if 'a' <= char <= 'z': #Verifies if character is lowercase
            return False #lowercase found, return False
    return True #lowercase not found, return True

