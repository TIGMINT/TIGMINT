import requests, urllib3
import os, re, argparse
from tqdm import tqdm
from sys import exit
from html import unescape
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urlparse
from urllib3.exceptions import InsecureRequestWarning

class downloader(object):
    def __init__(self, username, storiesFlag):
        self.username = username
        self.storiesFlag = storiesFlag
        self.api = 'https://storiesig.com'
        self.storiesLink = self.api + '/stories/' + self.username
        self.user = self.api + '?username=' + self.username
        self.root = requests.get(self.user, verify=False).text
        self.sdname = self.username + "_{}".format(datetime.now().strftime("%m%d%Y-%H%M%S"))

    def getStories(self):
        r = requests.get(self.storiesLink, verify=False).text
        if 'No stories to show' in r:
            print("[*] User '{}' did not post any recent story/stories!".format(self.username))
            os.rmdir(self.sdname)
            exit()

        stories = []
        print(stories)
        soup = BeautifulSoup(r, features="lxml")
        links =  soup.findAll('a', attrs={'href': re.compile("^https://scontent")})

        for link in links:
            url = link.get('href')
            stories.append(unescape(url))

        print('[*] Downloading last 24h stories...')
        try:
            for link in tqdm(links):
                url = link.get('href')
                r = requests.get(url, verify=False)
                parser = urlparse(url)
                filename = os.path.basename(parser.path)
                if not os.path.exists(self.sdname):
                    os.makedirs(self.sdname)
                with open(self.sdname + '/' + filename, 'wb') as f:
                    f.write(r.content)
                    f.close()
        except KeyboardInterrupt:
            exit()

    def getHighlights(self):
            hlarray = []
            hlnarray = []
            hnarray = []
            hdirname = []
            soup = BeautifulSoup(self.root, features="lxml")

            hlinks =  soup.findAll('a', attrs={'href': re.compile("^/highlights/")})
            for highlight in hlinks:
                url = highlight.get('href')
                parser = urlparse(url)
                hname = os.path.basename(parser.path)
                hlnarray.append(hname)
                hlarray.append(self.api + url)

            hnames = soup.findAll("img", {"class": "jsx-2521016335"})
            for i in hnames:
                dname = i['alt']
                hnarray.append(dname)

            for i, j in zip(hnarray, hlnarray):
                hdirname.append(i + '_' + j)

            dictionary = dict(zip(hlarray, hdirname))
            return dictionary

    def exists(self):
        if "Sorry, this username isn't available." in self.root:
            print("[*] User '{}' does not exist!".format(self.username))
            return False
        elif "This Account is Private" in self.root:
            print("[*] Account '{}' is private!".format(self.username))
            return False
        else:
            return True
    def downloadHighlight(self, key, value):
        html = requests.get(key, verify=False).text
        od = self.username + '/' + value
        os.mkdir(od)
        soup = BeautifulSoup(html, features="lxml")

        links =  soup.findAll('a', attrs={'href': re.compile("^https://scontent")})
        
        print('[*] Downloading highlight {} of {}...'.format(self.c,self.t))
        try:
            for link in tqdm(links):
                url = link.get('href')
                r = requests.get(url, verify=False)
                parser = urlparse(url)
                filename = os.path.basename(parser.path)

                with open(od + '/' + filename, 'wb') as f:
                    f.write(r.content)
                    f.close()
        except KeyboardInterrupt:
            exit()
    def validate(self):
        if not self.storiesFlag:
            if os.path.isdir(self.username):
                print("[*] Highlights for user '{}' are already downloaded!".format(self.username))
                exit()
            else:
                os.mkdir(self.username)
        else:
            os.mkdir(self.sdname)
def main():
    urllib3.disable_warnings(InsecureRequestWarning)
    # downloader('rakshit.tandon', 'stories')
    # args = usage()
    # print(args)
    usern = input()
    a= downloader(usern, 'True')
    a.getStories()
    # downloader.getStories(args.user)

# def usage():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-u','--user', nargs="?", help="Instagram username (required)", required=True)
#     parser.add_argument('-s', '--stories', dest="stories", action="store_true", help="Only download last 24h stories")
#     return parser.parse_args()


if __name__ == '__main__':
    main()