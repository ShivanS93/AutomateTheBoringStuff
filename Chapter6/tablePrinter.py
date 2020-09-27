#!python3

# tablePrinter.py - Prints a table that is aligned

example = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]



def printTable(tableData):

    colWidths = [0] * len(tableData)

    for i in range(len(tableData)):
        colWidths[i] = len(max(tableData[i], key=len))

    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(colWidths[x]),end=" ")


        print("")

def main():

    printTable(example)

if __name__ == '__main__':
    main()