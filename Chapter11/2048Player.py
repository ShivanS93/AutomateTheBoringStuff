#! python3
# 2048.py - Automate playing the 2048 game

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import logging, random as r

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def main():

    webpage = 'https://play2048.co'

    loops = 0

    browser = webdriver.Chrome()
    browser.get(webpage)

    htmlElem = browser.find_element_by_tag_name('html')

    def isGameOver():
        try:
            gameoverElem = browser.find_element_by_class_name('game-message.game-over')
        except NoSuchElementException:
            logging.debug("NO game over detected")
            return False
        logging.debug("Game is OVER")
        return True


    while not isGameOver():
        key_random = r.randint(1, 4)
        loops += 1
        if key_random == 1:
            logging.debug("DOWN")
            htmlElem.send_keys(Keys.DOWN)
        if key_random == 2:
            logging.debug("UP")
            htmlElem.send_keys(Keys.UP)
        if key_random == 3:
            logging.debug("RIGHT")
            htmlElem.send_keys(Keys.RIGHT)
        if key_random == 4:
            logging.debug("LEFT")
            htmlElem.send_keys(Keys.LEFT)

    scoreElem = browser.find_element_by_class_name('score-container')
    score = scoreElem.text
    print('Score: %s' % score)

    print('Loops: %s'% loops)
    input()
    browser.quit()

if __name__ == '__main__':
    main()

