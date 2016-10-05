from html.parser import HTMLParser
from urllib.parse import urljoin


class LinkManager(HTMLParser):
    all_links = set()
    special_links = set()

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if '/photo/show/' in str(attr[1]):
                    attri = urljoin('http://www.chictopia.com/', attr[1])
                    self.all_links.add(attri)

    def get_links(self):
        return self.all_links

    def get_special_links(self, tags):
        dictionary = {}
        for tag in tags:
            for link in self.all_links:
                if tag[:-1] in link[35:]:
                    dictionary[tag[:-1]] = [].append(link)
                    print(tag[:-1] + " ----> " + link)
