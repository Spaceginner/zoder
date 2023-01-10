from modules.pressor import compressor


def validate_jzdr(jzdr_image: dict):
    for i in range(2):
        for j in range(len(jzdr_image['matrix'][i])):
            if not jzdr_image['matrix'][i][j]:
                jzdr_image['matrix'][i][j].append(0)

    return jzdr_image


def print_ucnjzdr_image(ucnjzdr_image: list[list[bool]]):
    for y in range(len(ucnjzdr_image)):
        for x in range(len(ucnjzdr_image[0])):
            print('▓▓' if ucnjzdr_image[y][x] else '░░', end='')

        print()
