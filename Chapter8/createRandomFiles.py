#! python3

# createsRandomTxtFiles.py - creates random .txt files to test regexSearch.py

import os

def main():

    Names = ['Jon', 'Bill', 'Maria', 'Jenny', 'Jack']
    path = r'.\Chapter8\RegexSearch'

    import random as r

    for i in Names:
        creatingFile = open(os.path.join(path, '{}.txt'.format(i)), 'w')
        creatingFile.write('{} hit {} and called {} who attached {}.'
                        .format(Names[r.randint(0,len(Names)-1)],
                                Names[r.randint(0,len(Names)-1)],
                                Names[r.randint(0,len(Names)-1)],
                                Names[r.randint(0,len(Names)-1)]))
        creatingFile.close()

        print('Created {}.txt'.format(i))

if __name__ == '__main__':
    main()