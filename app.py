import os
from os.path import splitext
from pathlib import Path
import shutil

"""
What do I want to do
I want the application to go into my downloads folder and get all the different type of file extensions in my downloads folder. 

Then create directories for each extension type.

Iterate over the files and move them according to their extension.
"""

DOWNLOAD_DIR = f'{Path.home()}/Downloads'


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
    return extension_dict
            

def create_directories(ext_dict):
    for dir_name in ext_dict.values():
        extension_dir = f'{DOWNLOAD_DIR}/{dir_name}'
        if not os.path.isdir(extension_dir):
            os.mkdir(extension_dir)

def move_files_to_directory(download_dir_objs,ext_dict):
    for obj in download_dir_objs:
        curr_dir = f'{DOWNLOAD_DIR}/{obj}'
        file_ext = None
        extension_dir = None

        if is_file(obj):
            file_ext = get_file_extension(obj)

        # some files don't have extension
        # some objects are directories
        if file_ext == '' or file_ext is None:
            extension_dir = ext_dict['unknown']
        else:
            extension_dir = ext_dict[file_ext]
        
        final_dir = f'{DOWNLOAD_DIR}/{extension_dir}/{obj}'

        shutil.move(curr_dir,final_dir)
            
            


if __name__ == '__main__':
    objects_in_download_folder = os.listdir(DOWNLOAD_DIR)
    ext_dict = get_unique_file_extensions(objects_in_download_folder)

    create_directories(ext_dict)
    move_files_to_directory(objects_in_download_folder, ext_dict)


