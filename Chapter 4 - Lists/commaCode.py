# This function that takes a list value as an argument and returns a string with all the items separated by a comma and 
# a space, with and inserted before the last item.
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
# It will also handle empty lists, and lists with only a single value.

def commaCode(list):
    string = ""
    listLength = len(list)
    
    if listLength == 0:
        print('You passed an empty list!')

    elif listLength == 1:
        string = list[0]
        print(string + ".") 

    else:
        for i in range(listLength - 1):
            string += list[i] + ", "
        string += "and " + list[-1] + "."
        print(string)
        

spam = ['apples', 'bananas', 'tofu', 'cats']

emptyList = []

singleList = ["puppy"]

commaCode(emptyList)

commaCode(spam)

commaCode(singleList)
