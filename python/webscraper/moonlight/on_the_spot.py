import requests
from lxml import html




# print "status: ", r.status_code
# print r.headers['content-type']
# print r.encoding
# print r.text

def callback_hell(link):
    r = requests.get(link)
    tree = html.fromstring(r.text)
    arr = tree.xpath("//a")

    # try:
    for i in range(3):
        try:
            print arr[i].attrib['href']
            callback_hell(arr[0].attrib['href'])
        except Exception as e:
            print "error: ", e
    # except Exception as e:
        # print e

callback_hell("http://motherfuckingwebsite.com/")



























