import requests
import LinkManager


class ChictopiaDownloader:
    url = ''

    def __init__(self, url, init, end):
        self.url = url
        self.page_range(init, end)

    def page_range(self, init, end):
        parser = LinkManager.ChictopiaLinkFinder()
        for i in range(init, end):
            html_page = requests.get(self.url + '/' + str(i))
            parser.feed(html_page.text)
        return parser.get_links()
