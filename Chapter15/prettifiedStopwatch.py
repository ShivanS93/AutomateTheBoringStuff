#! python3
# prettfiedStopwatch.py - stopwatch that is pretty
# requirements, pyperclip

import time, pyperclip

def main():
    # create stopwatch lapNum, lapTime, totalTime Lap #lapNum: totalTime (lapTime)
    print('Press ENTER for lap times. Press CTRL+C to exit')
    input()
    print('START', end='\n')
    startTime = time.time()
    lapNum = 0
    clipboard = []

    while True:
        startLap = time.time()
        while True:
            input()
            break

        totalTime = round(time.time() - startTime, 2)
        lapNum += 1
        lapTime = round(time.time() - startLap, 2)

        lapNumString = str(lapNum).rjust(3, ' ')
        totalTimeString = str(totalTime).rjust(6,' ')
        lapTimeString = str(lapTime).rjust(5, ' ')

        print('Lap #%s: %s (%s)' % (lapNumString, totalTimeString, lapTimeString), end='')

        # pyperclip: store data so it can be
        clipboard.append('Lap #%s: %s (%s)' % (lapNumString, totalTimeString, lapTimeString))
        pyperclip.copy('\n'.join(line for line in clipboard))

if __name__ == '__main__':
    main()


