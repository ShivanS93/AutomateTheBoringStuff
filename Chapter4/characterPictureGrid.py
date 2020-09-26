#!python3

# characterPictureGrid.py - Create a heart shape using the grid below

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# x is down the above grid and y is across


#print(grid[0][0],end='')
#print(grid[1][0],end='')
#print(grid[2][0],end='')

def main ():
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print(grid[x][y], end='')
        print("")

if __name__ == '__main__':
    main()

# output:
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....
#