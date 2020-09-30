#! python3
# spam.py creates spam00x.txt files for a problems needed to solve for fillingInTheGaps.py
# for testing fillingInTheGaps.py

import os, random as r

def makeSpam(tail):
    spamname = 'spam' + tail.rjust(3,'0') + '.txt'
    return spamname

def main():

    listNum = list(range(1,101))
    ranlistNum = r.sample(listNum,50)

    p = 'Chapter9\spam'
    path = os.path.join(os.getcwd(),p)

    for i in ranlistNum:
        tail = str(i)
        filename = 'spam' + tail.rjust(3,'0') + '.txt'
        filepath = path + '\\' + filename
        file = open(filepath,'w')
        file.close()

if __name__ == '__main__':
    main()