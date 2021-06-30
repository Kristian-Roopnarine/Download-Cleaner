import os
from os.path import splitext
from pathlib import Path

"""
What do I want to do
I want the application to go into my downloads folder and get all the different type of file extensions in my downloads folder. 

Then create directories for each extension type.

Iterate over the files and move them according to their extension.
"""

DOWNLOAD_DIR = f'{Path.home()}/Downloads'

objects_in_download_folder = os.listdir(DOWNLOAD_DIR)

def is_file(file):
    return os.path.isfile(f'{DOWNLOAD_DIR}/{file}')

def get_file_extension(file):
    return splitext(file)[1]
    
def get_unique_file_extensions(files):
    suffix = '_downloads'
    extension_dict = {'unknown':'unknown_downloads'}
    for obj in files:
        if is_file(obj):
            file_ext = get_file_extension(obj)

            # some files do not have extensions
            if file_ext not in extension_dict and file_ext != '':
                extension_dict[file_ext] = file_ext + suffix
            
    print(extension_dict)
                
get_unique_file_extensions(objects_in_download_folder)


