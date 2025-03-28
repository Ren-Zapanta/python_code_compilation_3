#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
def custom_endswith(string, suffix): #Cutom function recreating endswith string manipulator
    
    string_length = len(string)  #gets the length of main string
    suffix_length = len(suffix)  #gets the length of the suffix
    
    if suffix_length > string_length: #Checks if sufficx is longer than the string. Returns false, if not
        return False
    
    string_end = string[string_length - suffix_length:] #extracts the ending part of the string with the same length as the suffix
    
    return string_end == suffix  #compares extracted part with suffix