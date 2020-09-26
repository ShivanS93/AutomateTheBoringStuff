#! python3
# commaCode.py - Create a function that prints a list with commas as a string

def giveList(someList):
    output = ""
    for i in someList:
        if i == someList[0]:
            output = str(i)
        else:
            output = output + ", " + str(i)

    return print(output)


def main():

    spam = ['apples', 'bananas', 'tofu', 'cats', 'brads', 'Tamz']
    
    giveList(spam)

if __name__ == "__main__":
    main()