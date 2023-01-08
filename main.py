import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='zoder',
        description='An experimental loss-less image compression algorithm'
    )

    parser.add_argument('mode', choices=['c', 'd'], help='c - compress; d - decompress')
    parser.add_argument('input', help='path to a file to be processed')

    parser.add_argument('-o', '--output', help='path to a file to be stored')

    return parser


def main(mode: str, input_filename: str, output_filename: str | None):
    if mode not in ['c', 'd']:
        raise ValueError(f'argument `mode` must be \'c\' or \'d\' not {mode}')
    if mode == 'd':
        raise NotImplementedError

    if output_filename is None:
        output_filename = input_filename + ".zdr"

    pass


if __name__ == '__main__':
    args = create_parser().parse_args()
    main(args.mode, args.input, args.output)
