def compress(ucnjzdr_image: list[list[bool]]) -> dict:
    size_x = len(ucnjzdr_image[0])
    size_y = len(ucnjzdr_image)

    unjzdr_image = [[[] for _ in range(size_x)], [[] for _ in range(size_y)]]

    # Vertical
    for x in range(size_x):
        block_size = 0
        for y in range(size_y):
            if ucnjzdr_image[y][x]:
                if block_size == 0:
                    block_size += 1
                elif ucnjzdr_image[y - 1][x]:
                    block_size += 1

                if y == size_y - 1 or not ucnjzdr_image[y + 1][x]:
                    unjzdr_image[0][x].append(block_size)
                    block_size = 0

    # Horizontal
    for y in range(size_y):
        block_size = 0
        for x in range(size_x):
            if ucnjzdr_image[y][x]:
                if block_size == 0:
                    block_size += 1
                elif ucnjzdr_image[y][x - 1]:
                    block_size += 1

                if x == size_x - 1 or not ucnjzdr_image[y][x + 1]:
                    unjzdr_image[1][y].append(block_size)
                    block_size = 0

    return {
        "version": 1,
        "matrix": unjzdr_image
    }
