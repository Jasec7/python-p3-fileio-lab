def text_path(name):
        name = str(name)
        if name.endswith('.txt'):
            return name
        else:
            return name + ".txt"

def write_file(file_name, file_content):
     path = text_path(file_name)
     with open(path, mode='w', encoding='utf-8') as file:
        file.write(file_content)


def append_file(file_name, append_content):
   path = text_path(file_name)
   with open(path, mode='a', encoding='utf-8') as file:
    file.write(append_content)
    
def read_file(file_name):
    path = text_path(file_name)
    with open(path, encoding='utf-8') as file:
        return file.read()