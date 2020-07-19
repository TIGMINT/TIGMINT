import insta_heighlight
import user_info
import sys
from zipfile import ZipFile
import os

username = sys.argv[1]

dataDir = user_info.Username(username)
print(dataDir)
insta_heighlight.main(username)
dataDir = dataDir.replace('\\','/')
os.chdir(dataDir)
if os.path.exists(username+"-data.zip"):
  os.remove(username+"-data.zip")
def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

            # returning all file paths
    return file_paths


def main():
    # path to folder which needs to be zipped
    directory = './'

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    # printing the list of all files to be zipped
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)

        # writing files to a zipfile
    with ZipFile(username+'-data.zip', 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')
if __name__ == '__main__':
    main()