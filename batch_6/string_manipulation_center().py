#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
user_input_string = input("Lagay ka string, sir: ") #Requests string input from user
user_input_length = int(input("Gaano kahaba mo po gusto, sir?: ")) #Requests desired user length

get_length = len(user_input_string) #gets the length of user's input string

if get_length < user_input_length:  #Verifies for the need of "padding"
    total_padding = user_input_length - get_length  #gets the total space needed
    left_padding = total_padding // 2  #Spaces for the left
    right_padding = total_padding - left_padding  #Spaces for the right

    output_string = (" " * left_padding) + user_input_string + (" " * right_padding)  # Construct the centered string
else:
    output_string = user_input_string  #long enough

print(f"'{output_string}'")  #print output, indicate spaces w/ single quotes