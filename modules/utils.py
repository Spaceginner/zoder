from modules.pressor import compressor


def validate_jzdr(jzdr_image: dict):
    for i in range(2):
        for j in range(len(jzdr_image['matrix'][i])):
            if not jzdr_image['matrix'][i][j]:
                jzdr_image['matrix'][i][j].append(0)

    return jzdr_image
