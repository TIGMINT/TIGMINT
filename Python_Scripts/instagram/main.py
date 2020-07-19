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
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


def main():
    directory = './'
    file_paths = get_all_file_paths(directory)
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
    with ZipFile(username+'-data.zip', 'w') as zip:
        for file in file_paths:
            zip.write(file)

    print('All files zipped successfully!')
if __name__ == '__main__':
    main()
