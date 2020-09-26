""" For linux the user must install exiftool using command sudo apt install exiftool """
import platform
import exiftool
import json
import os
curentOS = platform.system()
files = "bridge.jpg"

with exiftool.ExifTool() as et:
    if curentOS == "Windows":
        et.executable = os.getcwd() + "\exiftool"
    else:
        et.executable = "exiftool"

    metadata = et.get_metadata(files)
print(metadata)
with open('newMetaData.json', 'w') as fp:
    json.dump(metadata, fp, indent=4)