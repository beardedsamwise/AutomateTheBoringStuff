def printTable(table):
    # Find the longest string in the inner lists
    colWidths = [] # create empty array
    for list in table:
        index = (table.index(list)) # get the index of each inner list
        colWidths.append(0) # create a new zero value in list 
        for string in list:
            if len(string) > colWidths[index]: # check if current str is longer than what has been stored
                colWidths[index] = len(string) 
    # TODO print back data in tabular format using colWidths
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)