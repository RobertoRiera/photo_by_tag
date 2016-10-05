from html.parser import HTMLParser

import requests


class ImageDownloader(HTMLParser):
    url = ''

    def __init__(self, url):
        super().__init__()
        html = requests.get(url).text
        self.url = url
        self.feed(html)

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                print(attr)
