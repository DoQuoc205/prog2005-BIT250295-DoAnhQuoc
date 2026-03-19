import os
def get_filename(path):
    return os.path.basename(path)
def get_filename(path):
    return os.path.splitext(os.path.basename(path))[0]
path = r"d:\music\muabui.mp3"
print(get_filename(path))
print(get_filename(path))