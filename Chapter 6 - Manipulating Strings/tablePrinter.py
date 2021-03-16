def printTable(table):
    # Find the longest string in the inner lists
    colWidths = [] # create empty list
    for list in table:
        index = (table.index(list)) # get the index of each inner list
        colWidths.append(0) # create a new zero value in list 
        for string in list:
            if len(string) > colWidths[index]: # check if current str is longer than what has been stored
                colWidths[index] = len(string) 
    # Get column height and width
    width = len(table)
    height = 0
    for list in table:
        if (len(list) > height):
            height = len(list)
    # print back data in tabular format using colWidths
    for x in range(height):
        for y in range(width):
            print(table[y][x].rjust(colWidths[y]), end="  ")
        print("") # print a new line at the end 

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
