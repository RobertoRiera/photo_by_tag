import FileManager
from LinkManager import LinkManager

tags = FileManager.get_tags_from_file()
link_manager = LinkManager()
special_links = LinkManager.get_special_links(link_manager, tags)


url = 'http://www.chictopia.com/browse/new_photos/approve'
