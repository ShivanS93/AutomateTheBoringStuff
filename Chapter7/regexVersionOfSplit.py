#!python3

# regexVersionOfSplit.py - split a string by an argument

import re

def regexSplit(text, argument=''):

    if argument == '':
        textRegex = re.compile(r'\w+')
        return textRegex.findall(text)

    else:
        textRegex = re.compile(rf'{argument}')
        subMO = textRegex.search(text).span()
        return subMO

def main():
    
    # testString = 'Hello World'
    # testArgument = 'l'

    testString = input('Enter string to be split: ')
    helltestArgument = input('Enter argument to be split: ')

    useSplit = regexSplit(testString,testArgument)

    print(useSplit)

    try:
        print(testString.split(testArgument))
    except ValueError:
        print(testString.split())

if __name__ == '__main__':
    main()