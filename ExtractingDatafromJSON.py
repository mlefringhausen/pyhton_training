import json
import urllib
# http://python-data.dr-chuck.net/comments_42.json

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break
    print 'Retrieving data from ', url
    uh = urllib.urlopen(url)
    data = uh.read()
    info = json.loads(data)

    print 'comment count:', len(info)

    sum_count = 0
    for comment in info['comments']:
        sum_count += comment['count']
    print sum_count