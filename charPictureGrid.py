#############
# VARIABLES #
#############

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Determine the width and height of the nested list
# We're assuming that the width of each list is the same by only checking the first nested list

height = len(grid)
width = (len(grid[0]))

# Print the contents of the nested list, running through the first item of each nested list, then the second, etc.
# We'll also print a new line after each "row" is processed except for the first loop. 

for x in range(width):
        if x > 0:
                print(" ")
        for y in range(height):
            print(grid[y][x], end="")
print (" ")