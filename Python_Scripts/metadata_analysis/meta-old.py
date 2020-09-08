from PIL import Image
from PIL.ExifTags import TAGS
import json


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (bytes, bytearray)):
            return obj.decode("ASCII")
        return json.JSONEncoder.default(self, obj)


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    jsonified = json.dumps(ret, cls=MyEncoder, indent=4)
    with open('metadata.json', 'w') as fp:
        json.dump(jsonified, fp)
    print(ret)


get_exif("bridge.jpg")