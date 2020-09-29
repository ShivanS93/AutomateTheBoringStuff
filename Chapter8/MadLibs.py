#! python3

# MadLibs.py - allows user to add own text to a text file

import re

def main():

    # Create .txt file
    MadLibsFile = open('./Chapter8/MadLibs/MadLibs.txt', 'w')
    MadLibsFile.write('The ADJECTIVE panda walked to the NOUN and then VERB.'
                    ' A nearby NOUN was unaffected by these events')
    MadLibsFile.close()

    # Read from .txt file
    MadLibsFile = open('./Chapter8/MadLibs/MadLibs.txt', 'r')
    MadLibsText = MadLibsFile.read()
    MadLibsFile.close()

    # search through text file for occurances of ADJECTIVE, NOUN, VERB

    MadLibsRegex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)|(ADVERB)')

    MadLibsFindall = MadLibsRegex.findall(MadLibsText)
    print(MadLibsFindall)

    for i in MadLibsFindall:
        for j in i:
            if j != '':
                reg = re.compile(r'{}'.format(j))
                sub_text = input("Enter %s: " % j)
                MadLibsText = reg.sub(sub_text, MadLibsText, 1)

    # print(MadLibsText)

    # save to .txt file
    newMadLibsFile = open('./Chapter8/MadLibs/NewMadLibs.txt', 'w')
    newMadLibsFile.write(MadLibsText)
    newMadLibsFile.close()


    # read .txt file again

    newMadLibsFile = open('./Chapter8/MadLibs/NewMadLibs.txt', 'r')
    newMadLibsFileText = newMadLibsFile.read()

    print(newMadLibsFileText)
    newMadLibsFile.close()

if __name__ == '__main__':
    main()