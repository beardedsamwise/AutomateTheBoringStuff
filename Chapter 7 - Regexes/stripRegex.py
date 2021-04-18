# Write a function that takes a string and does the same thing as the strip() string method. 
# If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. 
# Otherwise, the characters specified in the second argument to the function will be removed from the string.

def stripRegex(string, chars=""):
    # TO DO - create regex for alphanumerics and seperately blank spaces

    # TO DO - write logic to print string without blank spaces if chars is not passed
    #       - if chars is passed replace blank spaces with chars

    #testing
    print(string)
    if chars:
        print(chars)

stripRegex("Luke jumps on a pogo stick")
stripRegex("Peter likes foxes","_")