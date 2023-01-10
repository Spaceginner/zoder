import json
import os.path

from PIL import Image

from modules.coder import encoder, decoder
from modules.pressor import compressor, decompressor


def test(element: str) -> int:
    if element not in ['enc', 'dec', 'com', 'decom']:
        raise ValueError

    # Encoding
    if element == 'enc':
        return _enc()
    elif element == 'dec':
        return _dec()
    elif element == 'com':
        return _com()
    elif element == 'decom':
        return _decom()


def _enc():
    check = json.load(open(os.path.join("test", "image.ucnjzdr")))
    answ = encoder.encode(Image.open(os.path.join('test', 'image.png')))

    return check == answ

def _dec():
    check = Image.open(os.path.join("test", "image.png"))
    answ = decoder.decode(json.load(open(os.path.join("test", "image.ucnjzdr"))))

    is_same = True
    for y in range(check.size[1]):
        for x in range(check.size[0]):
            if check.getpixel((x, y)) != answ.getpixel((x, y)):
                is_same = False
                break

    return is_same

def _com():
    check = json.load(open(os.path.join("test", "image.jzdr")))
    answ = compressor.compress(json.load(open(os.path.join("test", "image.ucnjzdr"))))

    return check == answ

def _decom():
    check = json.load(open(os.path.join('test', 'image.ucnjzdr')))
    answ = decompressor.decompress(json.load(open(os.path.join('test', 'image.jzdr'))))

    return check == answ
