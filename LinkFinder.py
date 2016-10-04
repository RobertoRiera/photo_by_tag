from html.parser import HTMLParser
from urllib.parse import urljoin


class LinkFinder(HTMLParser):
    links = set()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if '/photo/show/' in str(attr[1]):
                    attri = urljoin('http://www.chictopia.com/', attr[1])
                    self.links.add(attri)

    def get_links(self):
        return self.links
