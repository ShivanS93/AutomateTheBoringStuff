#!python3

# theCollatzSequence.py - This uses the Collatz Sequence on an input.

# Rules:
# if num is even, then return num // 2
# if num is off, then return 3 * num + 1
# this will always lead to one
# with input validation

def collatz(num):
    '''
    num - number to be added to the collatz sequence
    '''
    if num == 1:
        return
    elif num % 2 == 0:      # num is even
        ans = num // 2
        print(ans)
        collatz(ans)
    elif num % 2 == 1:      # num is odd
        ans = 3 * num + 1
        print(ans)
        collatz(ans)
    return ans

def main():
    try:
        num = int(input('Please enter a number:\n'))
        collatz(num)
    except:
        print('Please provide an interger.')
        main()

    return

if __name__  == "__main__":
    main()