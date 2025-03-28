#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
user_input = input("Please enter a statement: ") #Asks the user for an input

words = user_input.split() #splits the input 

formatted_words = [] #initializes empty string

for word in words: #loops through each word and capitalizes every first letter
    if word: #Verifies if the word is empty

        formatted_word = word[0].upper() + word[1:].lower()
        formatted_words.append(formatted_word)

formatted_text = " ".join(formatted_words) #Joins back the words

print(formatted_text) #Prints result