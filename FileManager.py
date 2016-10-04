import os


def create_tag_directory():
    project_path = os.path.realpath(".")
    tag_path = os.path.join(project_path, 'Photos')
    if os.path.exists(tag_path):
        tags = open('tags.txt', 'r')
        for tag in tags:
            if not os.path.exists(os.path.join(tag_path, tag[:-1])):
                print("Creado el directorio -> "+ os.path.join(tag_path, tag))
                os.mkdir(os.path.join(tag_path, tag[:-1]))
        tags.close()
    else:
        os.mkdir('Photos')
        tags = open('tags.txt', 'r')
        for tag in tags:
            if not os.path.exists(os.path.join(tag_path, tag)):
                os.mkdir(os.path.join(tag_path, tag[:-1]))
        tags.close()
