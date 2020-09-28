#!python3

# strongPasswordDetection.py - as the name suggestion

import re

#  password must have 8 chars with lowercase, Uppercase and at least on number

def passwordChecker(passWord):

    passWord = str(passWord)

    lowerRegexMo = re.compile(r'[a-z]').search(passWord)
    upperRegexMo = re.compile(r'[A-Z]').search(passWord)
    numberRegexMo = re.compile(r'[0-9]').search(passWord)

    if lowerRegexMo == None:
        print("The password must contain lower case letters")

    if upperRegexMo == None:
        print("The password must contain UPPER case letters")

    if numberRegexMo == None:
        print("The password must contain numbers")

    if len(passWord) < 8:
        print("The password must have at least 8 characters")

    elif lowerRegexMo != None and upperRegexMo != None and numberRegexMo != None and len(passWord) > 8:
        print('\"' + passWord + '\"' + " is STRONG!")
        return True

    return False


def main():
    tests = str(input('Enter Password: '))

    check = passwordChecker(tests)

    if not check:
        main()

if __name__ == "__main__":
    main()