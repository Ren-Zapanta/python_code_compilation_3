#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
user_input_string = input("Lagay ka string, sir: ") #Requests string input from user
user_input_length = int(input("Gaano kahaba mo po gusto, sir?: ")) #Requests desired user length
get_length = len(user_input_string) #gets the length of user's input string

if get_length < user_input_length: #checks which is bigger between desired length and actual string length
    padding = " " * (user_input_length - get_length)  #Creates the required spaces to match the desired length
    output_string = user_input_string + padding # Concatenates the original string with spaces
else:
    output_string = user_input_string

print(output_string) #Prints result
