import FileManager
import requests
from LinkManager import LinkManager
from time import sleep


class ChictopiaDownloader:
    base_url = 'http://www.chictopia.com/browse/new_photos/approve'
    tags = set()
    special_links = set()
    parser = None

    def __init__(self, init, end):
        FileManager.FileManager().create_tag_directory()
        self.tags = FileManager.get_tags_from_file()
        self.parser = LinkManager()
        self.page_range(init, end)
        self.special_links = self.parser.get_special_links(self.tags)

    def page_range(self, init, end):
        for i in range(init, end):
            actual_url = self.base_url + '/' + str(i)
            html = requests.get(actual_url).text
            sleep(0.1)
            self.parser.feed(html)
