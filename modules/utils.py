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


def create_ucnjzdr_image(size_x: int, size_y: int, state: int = 0, default: bool = False):
    max_state = 2 ** (size_x * size_y) - 1

    if state > max_state:
        raise ValueError(f'maximal value of the argument `state` with the an image size of {size_x}x{size_y} is {max_state} (total states: {max_state + 1})')

    ucnjzdr_image = [[default for _ in range(size_x)] for _ in range(size_y)]

    for _ in range(state):
        ucnjzdr_image = iterate_ucnjzdr_image(ucnjzdr_image)

    return ucnjzdr_image


def iterate_ucnjzdr_image(ucnjzdr_image: list[list[bool]]):
    is_exiting = False
    for y in range(len(ucnjzdr_image)):
        for x in range(len(ucnjzdr_image[0])):
            if ucnjzdr_image[y][x]:
                ucnjzdr_image[y][x] = False
            else:
                ucnjzdr_image[y][x] = True
                is_exiting = True
                break

        if is_exiting:
            break

    return ucnjzdr_image
