import os


class FileManager:
    special_tags = []

    def __init__(self):
        self.special_tags = get_tags_from_file()

    def create_tag_directory(self):
        project_path = os.path.realpath(".")
        tag_path = os.path.join(project_path, 'Photos')
        if os.path.exists(tag_path):
            for tag in self.special_tags:
                if not os.path.exists(os.path.join(tag_path, tag[:-1])):
                    print("Creado el directorio -> " + os.path.join(tag_path, tag))
                    os.mkdir(os.path.join(tag_path, tag[:-1]))
        else:
            os.mkdir('Photos')
            for tag in self.special_tags:
                os.mkdir(os.path.join(tag_path, tag[:-1]))


def get_tags_from_file():
    return open('tags.txt', 'r')
