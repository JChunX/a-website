
def read_markdown_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content