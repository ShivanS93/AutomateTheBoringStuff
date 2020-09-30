#! python3
# fillInTheGaps.py - locate a gap in the sequence of files and rename the files to fill in these gaps
# uses spam.py to create spam files to test on

import os, re, shutil

p = 'Chapter9\spam'
path = os.path.join(os.getcwd(), p)

def numSuffixMatch(filename):
    numSuffixMatch = re.compile(r'^(spam)(\d\d\d)(\.txt)$')
    mo = numSuffixMatch.search(filename)

    return mo.group(2)

def main():

    # get list of txt files
    files = os.listdir(path)
    files.sort()

    #  regex to get numbers
    for i in range(len(files)):

        #files = os.listdir(path)

        try:
            if int(numSuffixMatch(files[i+1])) != int(numSuffixMatch(files[i])) + 1:
                newtail = str(int(numSuffixMatch(files[i])) + 1)
                newFileName = 'spam' + newtail.rjust(3, '0') + '.txt'
                oldFileName = files[i+1]
                files[i+1] = newFileName
                print('%s changed to %s' %(path + '\\' + oldFileName,path + ' \\' + newFileName))
                shutil.move(path + '\\' + oldFileName,path + '\\' + newFileName)
        except IndexError:
            continue

    # TODO add number

    numToAdd = str(int(input('Enter number: ')))
    checkPath = path + '\\' + 'spam' + numToAdd.rjust(3, '0')
    files = os.listdir(path)
    files.sort()
    files.reverse()

    print(files)


    for i in range(len(files)):
        if os.path.exists(checkPath):
            pass

if __name__ == '__main__':
    main()