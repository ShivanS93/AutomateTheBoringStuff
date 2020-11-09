#! python3
# webComicDownloader.py - Checks website and automatically downloads
# image since last visit
# Shivan Sivakumaran

import os
import logging
import requests, bs4
import time, datetime

#logging.basicConfig(filename='log.txt', level=logging.DEBUG,
#                    format='%(asctime)s - %(levelname)s - %(messages)s')

url = 'https://samharith.com/'
savePath = 'Chapter15\\Download'
os.makedirs(savePath, exist_ok=True)


# use requests and bs4 to access webpage and parse for image files to download

res = requests.get(url)
res.raise_for_status()

samHarithSoup = bs4.BeautifulSoup(res.text, features='html.parser')

imgElem = samHarithSoup.select('#content img')
timeElem = samHarithSoup.select('#content time')

imageURL = imgElem[0].get('src')
res = requests.get(imageURL)
res.raise_for_status()

# save image file to file location

logging.debug("Successful")
imageFile = open(os.path.join(savePath,os.path.basename(imageURL)), 'wb')
for chunk in  res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()


# store time on a .txt file for when last retrieval was made by day
timeFile = open(os.path.join(savePath,'time.txt'), 'a')

dt = datetime.datetime.now()

y, m, d = dt.year, dt.month, dt.day
hr, min, sec = dt.hour, dt.minute, dt.second
timeFile.write("Downloaded %s... at %s/%s/%s %s:%s:%s"
      % (os.path.basename(imageURL), d, m, y, hr, min, sec))
timeFile.close()


