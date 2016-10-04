import os


class FileManager:
    special_tags = None

    def _init(self):
        self.special_tags = get_tags_from_file()

    def create_tag_directory(self):
        project_path = os.path.realpath(".")
        tag_path = os.path.join(project_path, 'Photos')
        if os.path.exists(tag_path):
            tags = self.special_tags
            for tag in tags:
                if not os.path.exists(os.path.join(tag_path, tag[:-1])):
                    print("Creado el directorio -> " + os.path.join(tag_path, tag))
                    os.mkdir(os.path.join(tag_path, tag[:-1]))
            tags.close()
        else:
            os.mkdir('Photos')
            tags = self.special_tags
            for tag in tags:
                if not os.path.exists(os.path.join(tag_path, tag)):
                    os.mkdir(os.path.join(tag_path, tag[:-1]))
            tags.close()


def get_tags_from_file():
    special_tags = open('tags.txt', 'r')
    return special_tags
