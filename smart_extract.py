import os
import shutil

'''
    For the given path, get the List of all files in the directory tree and move them to specified location. 
    Bonus: Also removes all empty folders left behind.
'''


def list_files(src_dir):
    file_list = os.listdir(src_dir)
    all_file_paths = list()
    # Iterate over all the entries
    for file_path in file_list:
        # Create full path
        full_file_path = os.path.join(src_dir, file_path)
        # If file_path is a directory then get the list of files in this directory
        if os.path.isdir(full_file_path):
            all_file_paths = all_file_paths + list_files(full_file_path)
        else:
            all_file_paths.append(full_file_path)

    return all_file_paths


def move_file_from_src_to_dest(file_path, dest_dir):
    src_file_dir = os.path.dirname(file_path)
    print('...looking for files in: ' + src_file_dir)

    if src_file_dir != dest_dir:
        print('...moving file(s) from: ' + src_file_dir + ' to: ' + dest_dir)
        dest_dir_path = os.path.join(dest_dir, os.path.basename(file_path))
        shutil.move(file_path, dest_dir_path)


def remove_empty_dirs(path, remove_root=True):
    if not os.path.isdir(path):
        return

    files = os.listdir(path)
    if len(files):
        for f in files:
            full_file_path = os.path.join(path, f)
            if os.path.isdir(full_file_path):
                remove_empty_dirs(full_file_path)

    # if folder empty, delete it
    if len(files) == 0 and remove_root:
        print('Removing empty folder:', path)
        os.rmdir(path)


def main():
    # destination path. Change here as per convenience.
    dest_dir = os.getcwd()

    # source path. Change here as per convenience.
    src_dir = os.getcwd()

    # Get the list of all files in directory tree at given path
    all_files = list_files(src_dir)

    # move file from src to dest (only if source n destination aren't same)
    for file_path in all_files:
        move_file_from_src_to_dest(file_path, dest_dir)

    # Function to remove empty folders
    remove_empty_dirs(dest_dir, False)


if __name__ == '__main__':
    main()
