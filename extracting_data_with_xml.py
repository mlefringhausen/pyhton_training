# http://python-data.dr-chuck.net/comments_42.xml
import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break
    print 'Retrieving data from ', url
    uh = urllib.urlopen(url)
    data = uh.read()
    tree = ET.fromstring(data)

    sum_count = 0
    counts = tree.findall('.//count')
    for count in counts:
        sum_count += int(count.text)

    print sum_count
