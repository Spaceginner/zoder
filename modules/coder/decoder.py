from PIL import Image


def decode(ucnjzdr_image: list[list[bool]]) -> Image.Image:
    image = Image.new('RGB', (len(ucnjzdr_image[0]), len(ucnjzdr_image)))

    for y in range(len(ucnjzdr_image)):
        for x in range(len(ucnjzdr_image[0])):
            image.putpixel((x, y), (0, 0, 0) if ucnjzdr_image[y][x] else (255, 255, 255))

    return image
