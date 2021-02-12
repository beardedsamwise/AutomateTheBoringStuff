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

height = len(grid)
width = (len(grid[0]))

# Print the contents of the nested list, running through the first item of each nested list, then the second, etc.
# We'll also print a new line after each "row" is processed except for the first loop. 

for x in range(width):
        if x > 0:
                print("\n")
        for y in range(height):
            print(grid[y][x], end="")
print ("\n")
