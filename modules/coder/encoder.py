from PIL import Image


def encode(image: Image.Image) -> list[list[bool]]:
    seq_image = list(image.convert('RGB').getdata(0))
    ims_image = [seq_image[i] != 255 for i in range(len(seq_image))]

    ucnjzdr_image = [[bool()] * image.size[0] for _ in range(image.size[1])]

    x_res = image.size[0]
    for i in range(len(ims_image)):
        ucnjzdr_image[i // x_res][i % x_res] = ims_image[i]

    # for y in range(image.size[1]):
    #     for x in range(image.size[0]):
    #         print('▓▓' if ucnjzdr_image[y][x] else '░░', end='')
    # 
    #     print()

    return ucnjzdr_image
