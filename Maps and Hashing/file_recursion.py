import os

#list of paths from files ending with the suffix
list_files = []
def find_files(suffix, path):
    #list of directories and files in the path
    dirs = os.listdir(path)
    for dir in dirs:
        new_path = os.path.join(path, dir)
        #check if the new path is a directory or a file with de suffix ending
        if os.path.isdir(new_path):
            find_files(suffix, new_path)
        elif os.path.isfile(new_path) and dir[-2:] == suffix:
            list_files.append(new_path)
    return list_files

print(find_files('.c', 'testdir'))
