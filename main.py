import argparse
import json

from PIL import Image

from modules import testing
from modules.coder import encoder
from modules.pressor import compressor


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='zoder',
        description='An experimental lossless image compression algorithm'
    )

    parser.add_argument('mode', choices=['c', 'd'], help='c - compress; d - decompress')
    parser.add_argument('-i', '--input', help='path to a file to be processed', required=True)

    parser.add_argument('-o', '--output', help='path where to store compressed file')
    parser.add_argument('-x', '--experimental', help='store file in experimental format', action='store_true')

    parser.add_argument('--test', action='store_true')

    return parser


def main(mode: str, input_filename: str, output_filename: str | None, experimental: bool, test: bool):
    if mode not in ['c', 'd']:
        raise ValueError(f'argument `mode` must be \'c\' or \'d\' not {mode}')
    if mode == 'd':
        raise NotImplementedError
    if experimental:
        raise NotImplementedError

    if test:
        for elem in ['enc', 'com']:
            print(f'Test result for {elem}: {"success" if testing.test(elem) else "fail"}')
    else:
        if output_filename is None:
            output_filename = input_filename + (".zdr" if experimental else ".jzdr")

        image = Image.open(input_filename)

        ucnjzdr_image = encoder.encode(image)
        jzdr_image = compress.compress(ucnjzdr_image)

        with open(output_filename, 'w') as io_stream:
            json.dump(jzdr_image, io_stream, indent=None)


if __name__ == '__main__':
    args = create_parser().parse_args()
    main(args.mode, args.input, args.output, args.experimental, args.test)
