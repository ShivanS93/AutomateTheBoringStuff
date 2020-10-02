#! python3
# linkVerfication.py - verfies link in a page and marks any 404s

import bs4, requests, os, logging
from requests import exceptions
from time import sleep
from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def main():

    sitemapURL = 'https://shivansivakumaran.com/sitemap' # starting url
    initialURL = 'https://shivansivakumaran.com'

    now = datetime.now()
    now_string = now.strftime('%d/%m/%Y %H:%M:%S')

    checked_links = []

    path = 'website'

    os.makedirs(path, exist_ok=True)

    the404sTxt = open(os.path.join(path, 'found404s.txt'), 'w')
    the404sTxt.write('\n%s\n' % (now_string))
    the404sTxt.write('404s found when crawling website: %s... using sitemap located: %s...\n' % (initialURL,sitemapURL))
    the404sTxt.close()

    crawledTxt = open(os.path.join(path, 'crawled.txt'), 'w')
    crawledTxt.write('\n%s\n' % (now_string))
    crawledTxt.write('Crawled pages and links tested when crawling website: %s... using sitemap located: %s..\n'
                    % (initialURL,sitemapURL))
    crawledTxt.close()

    def findLinks(url): # returns all links in a page

        print('Finding links in %s...' % url)

        link_list = []
        while True:
            try:
                sleep(5)                    # need to use sleep() or server will block / stops spamming the server
                res = requests.get(url)
                res.raise_for_status()
                break
            except HTTPError as e:
                if int(e.response.status_code) == 404:
                    print('404 link found: %s...' % url)
                    the404s.append(url)
                    return


        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        aElems = soup.select('a[href]')
        for i in range(len(aElems)):
            link = aElems[i].get('href')
            if link not in link_list: # prevents repeats
                if link.startswith('http'): # only crawls links
                    link_list.append(link)

        print('Links found: %s' % (link_list))
        return link_list


    # Download webpage and find a tags and href
    def checkLink(url):
        print('Checking %s....' % url)
        checked_links.append(url)
        while True:
            try:
                sleep(5)
                res = requests.get(url)
                res.raise_for_status() # checks if page exists if not this is 404
                return True
            except requests.exceptions.HTTPError:
                return False
            except requests.exceptions.ConnectionError:
                print("Connection refused... Try again")
                continue
        return

    crawl_list = findLinks(sitemapURL)

    for page in crawl_list:
        if page.startswith(initialURL):  # will only crawl through links for parent webpage
            links_in_page = findLinks(page) # find links in each website page
            for link in links_in_page:
                if link not in checked_links:
                    crawledTxt = open(os.path.join(path, 'crawled.txt'), 'a')
                    crawledTxt.write('Link: %s in Page: %s\n' % (link, page))
                    crawledTxt.close()
                    if not checkLink(link):
                        print("%s is a 404 link, located in %s" % (link, page))
                        the404sTxt = open(os.path.join(path, 'found404s.txt'), 'a')
                        the404sTxt.write('%s... location: %s\n' % (link, page))
                        the404sTxt.close()
                    else:
                        print("%s healthy" % (link))
                else:
                    print('%s already checked' % link)

if __name__ == '__main__':
    main()


