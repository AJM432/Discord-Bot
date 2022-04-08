
import requests
from bs4 import BeautifulSoup as bs
import re
import json

def is_url(url):
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def find_image(topic):

    url = "https://www.bing.com/images/search?q="
    topic = '+'.join(topic.split())
    adlt = 'strict'
    count = 1
    url='https://bing.com/images/search?q=' + topic + '&safeSearch=' + adlt + '&count=' + str(count)
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    res = requests.get(url, headers=headers)
    soup = bs(res.content, 'html.parser')

    # images = soup.find_all('a',class_='iusc')
    # for image in images:

    #   print(image.get('m'))
    images = soup.find('a',class_='iusc')

    m = json.loads(images["m"])
    url = m["turl"]
    return url

if __name__ == "__main__":
  print(find_image('space'))
