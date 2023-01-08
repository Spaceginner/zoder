from PIL import Image


def encode(image: Image.Image) -> list[list[bool]]:
    seq_image = list(image.convert('RGB').getdata(0))
    ims_image = [seq_image[i] != 255 for i in range(len(seq_image))]

    ucnzdr_image = [[bool() for _ in range(image.size[0])] for _ in range(image.size[1])]
    i = 0
    for x in range(image.size[1]):
        for y in range(image.size[0]):
            ucnzdr_image[x][y] = ims_image[i]
            i += 1

    # for x in range(image.size[1]):
    #     for y in range(image.size[0]):
    #         print('▓▓' if ucnzdr_image[x][y] else '░░', end='')
    #
    #     print()

    return ucnzdr_image
