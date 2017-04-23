import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
position = raw_input('Enter position: ')


def get_link(position, tags):
    link_count = 0
    for tag in tags:
        link_count += 1
        if link_count == int(position):
            url1 = tag.get('href', None)
    return url1


def suppy(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    return tags


for i in range(int(count)):

    tags = suppy(url)
    url = get_link(position, tags)
    print(url)
