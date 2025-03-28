#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
sample_text = "For inspiration lang" #Sample string 
sample_suffix = "lang" #Sample suffix

suffix_length = len(sample_suffix) #Gets suffix length
last_part = sample_text[-suffix_length:] #Gets the last part of the string 

if last_part == sample_suffix: #Compares the ending part with sample_suffix variable
#prints corresponding result
    print("True")
else:
    print("False")