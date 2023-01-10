from modules import utils


# TODO make decompress() less garbage and more *intelligent* ie more generalized
def decompress(jzdr_image: dict) -> list[list[bool]]:
    if jzdr_image['version'] == 1:
        ucnjzdr_image = [[bool() for _ in range(len(jzdr_image['matrix'][0]))] for _ in range(len(jzdr_image['matrix'][1]))]

        # Stage one: filling semi-full and full lines

        # for x in range(len(ucnjzdr_image[0])):
        #     if jzdr_image['matrix'][0][x][0] == len(ucnjzdr_image):
        #         for i in range(len(jzdr_image['matrix'][0][x])):
        #             dsr_block_size = jzdr_image['matrix'][0][x][i]
        #
        #             for y in range(dsr_block_size):
        #                 ucnjzdr_image[y][x] = True
        #
        #         jzdr_image['matrix'][0][x].pop(0)
        #
        # jzdr_image = utils.validate_jzdr(jzdr_image)
        #
        # for y in range(len(ucnjzdr_image)):
        #     if jzdr_image['matrix'][1][y][0] == len(ucnjzdr_image[0]):
        #         for i in range(len(jzdr_image['matrix'][1][y])):
        #             dsr_block_size = jzdr_image['matrix'][1][y][i]
        #
        #             for x in range(dsr_block_size):
        #                 ucnjzdr_image[y][x] = True
        #
        #         jzdr_image['matrix'][1][y].pop(0)
        #
        # jzdr_image = utils.validate_jzdr(jzdr_image)

        for x in range(len(ucnjzdr_image[0])):
            if sum(jzdr_image['matrix'][0][x]) + len(jzdr_image['matrix'][0][x]) - 1 == len(ucnjzdr_image):
                offset = 0

                for i in range(len(jzdr_image['matrix'][0][x])):
                    dsr_block_size = jzdr_image['matrix'][0][x][i]
                    offset += dsr_block_size

                    for y in range(dsr_block_size):
                        ucnjzdr_image[y + offset - dsr_block_size + i][x] = True

                jzdr_image['matrix'][0][x] = [0, ]

        jzdr_image = utils.validate_jzdr(jzdr_image)

        for y in range(len(ucnjzdr_image)):
            if sum(jzdr_image['matrix'][1][y]) + len(jzdr_image['matrix'][1][y]) - 1 == len(ucnjzdr_image[0]):
                offset = 0

                for i in range(len(jzdr_image['matrix'][1][y])):
                    dsr_block_size = jzdr_image['matrix'][1][y][i]
                    offset += dsr_block_size

                    for x in range(dsr_block_size):
                        ucnjzdr_image[y][x + offset - dsr_block_size + i] = True

                jzdr_image['matrix'][1][y] = [0, ]

        jzdr_image = utils.validate_jzdr(jzdr_image)

        # Stage two: pure *magic* and hope
        # TODO add check for continuity of the block
        # (currently it only checks collisions)
        # WARNING complete garbage-code is coming
        # Vertical
        for x in range(len(ucnjzdr_image[0])):
            des_sum = 0
            for some_var in jzdr_image['matrix'][0][x]:
                des_sum += some_var

            act_sum = 0
            for y in range(len(ucnjzdr_image)):
                if ucnjzdr_image[y][x]:
                    if act_sum == 0:
                        act_sum += 1
                    elif ucnjzdr_image[y - 1][x]:
                        act_sum += 1

            if act_sum < des_sum:
                for y in range(len(ucnjzdr_image[0])):
                    des_sum_1 = 0
                    for some_var in jzdr_image['matrix'][1][y]:
                        des_sum_1 += some_var

                    act_sum_1 = 0
                    for test_x in range(len(ucnjzdr_image[0])):
                        if ucnjzdr_image[y][test_x]:
                            if act_sum_1 == 0:
                                act_sum_1 += 1
                            elif ucnjzdr_image[y][test_x - 1]:
                                act_sum_1 += 1

                    if des_sum_1 <= act_sum_1:
                        continue
                    else:
                        # here implement check for continuity

                        block_size = 0
                        for test_test_x in range(x + 1):
                            if ucnjzdr_image[y][test_test_x]:
                                if block_size == 0:
                                    block_size += 1
                                elif ucnjzdr_image[y][test_test_x - 1]:
                                    block_size += 1

                                if test_test_x == len(ucnjzdr_image[0]) - 1:
                                    block_size = 0

                        if block_size < jzdr_image['matrix'][1][y][0] or not ucnjzdr_image[y][x - 1]:
                            ucnjzdr_image[y][x] = True
                        else:
                            continue


        return ucnjzdr_image
