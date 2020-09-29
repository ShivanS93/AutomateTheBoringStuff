#! python3

# regexSearch.py - opens all .txt files for any line that matches the user-supplied regex
# createRandomFiles.py - creates files

import re, os


def main():

    # get user regex input
    userRegex = input('Please input regex: ')

    # open all .txt that match user regex

    # get a list of files in a current directory
    path = r'.\Chapter8\RegexSearch'
    file_list = os.listdir(path)
    # print(file_list)

    # get .txt files from file_list

    txt_list = []

    for file in file_list:
        txt_listRegex = re.compile(rf'^{userRegex}\.txt$')
        mo = txt_listRegex.search(file)
        if mo != None:
            file = open(os.path.join(path, file), 'r')
            content = file.read()
            print(mo.group(), end=' >>> ')
            print(content)
            file.close()

if __name__ = '__main__':
    main()