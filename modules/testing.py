import json
import os.path

from PIL import Image

from modules.coder import encoder


def test(element: str) -> int:
    if element not in ['enc', 'dec', 'com', 'decom']:
        raise ValueError

    # Encoding
    if element == 'enc':
        return _enc()


def _enc():
    check = json.load(open(os.path.join("test", "riwers", "encode.json")))
    answ = encoder.encode(Image.open(os.path.join('test', 'resources', 'encode.png')))

    return check == answ
