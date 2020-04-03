import os, time
import shutil
from datetime import datetime

'''
    For the given path, get the List of all files in the directory tree and rename them by specific format. 
'''


def list_files(src_dir):
    file_list = os.listdir(src_dir)
    all_file_paths = []

    # Iterate over all the entries
    for file_name in file_list:
        # Create full path
        full_file_path = os.path.join(src_dir, file_name)

        # If file_path is a directory then get the list of files in this directory
        if os.path.isdir(full_file_path):
            all_file_paths = all_file_paths + list_files(full_file_path)
        else:
            all_file_paths.append(full_file_path)

    return all_file_paths


def rename_file_from_src(file_path, postfix):
    file_dir = os.path.dirname(file_path)

    file_name = os.path.basename(file_path)
    name, ext = os.path.splitext(file_name)

    lmd_raw = time.ctime(os.path.getmtime(file_path))
    lmd_obj = datetime.strptime(lmd_raw, "%a %b %d %H:%M:%S %Y")
    lmd_formatted = lmd_obj.strftime("%Y%m%d")

    if postfix:
        new_name = "{} {} [{}]{}".format(lmd_formatted, name, postfix, ext)
    else:
        new_name = "{} {}{}".format(lmd_formatted, name, ext)

    file_path_new = os.path.join(file_dir, new_name)

    if file_name != 'batch_rename.py':
        print("Renamed `{}` :::: to :::: `{}`".format(file_name, new_name))
        os.rename(file_path, file_path_new)


def main():
    postfix = raw_input("Enter a desired postfix for the files (HR, SEC etc.) or leave blank.\n")

    if postfix:
        print("Renaming all files to the following format: YYYYMMDD <file_name> [{}].".format(postfix))
    else:
        print("Renaming all files to the following format: YYYYMMDD <file_name>")

    # current directory in source path. Change here as per convenience.
    src_dir = os.getcwd()

    # Get the list of all files in directory tree at given path
    all_files = list_files(src_dir)

    # rename file from src by appending lmd in front :: (LMD_<file_name> [HR,SEC])
    for file_path in all_files:
        rename_file_from_src(file_path, postfix)


if __name__ == '__main__':
    main()