from html.parser import HTMLParser
import urllib.request
import requests


class ImageDownloader(HTMLParser):
    url = ''
    name = ''
    tag = ''

    def __init__(self, url, tag, name):
        super().__init__()
        html = requests.get(url).text
        self.url = url
        self.name = name
        self.tag = tag
        self.feed(html)

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src' and '400.jpg' in attr[1]:
                    path = 'Photos/' + self.tag + '/' + self.name + '.jpg'
                    urllib.request.urlretrieve(attr[1], path)
