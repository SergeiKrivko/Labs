from PIL import Image
import struct


def encrypt_image(string: str, path):
    image = Image.open(path)
    size = image.size
    if len(string) + 8 > size[0] * size[1] // 3:
        raise OverflowError("too long string for this image")

    pixels = image.load()

    string = string.encode('utf-8')
    string = struct.pack("I", len(string)) + string + "\0".encode()

    byte_number = 0
    current_step = 0
    for i in range(size[0]):
        for j in range(size[1]):
            byte = string[byte_number]
            if current_step == 0:
                pixels[i, j] = modify_pixel(pixels[i, j], (byte & 128) >> 7, (byte & 64) >> 6, (byte & 32) >> 5)
                current_step += 1
            elif current_step == 1:
                pixels[i, j] = modify_pixel(pixels[i, j], (byte & 16) >> 4, (byte & 8) >> 3, (byte & 4) >> 2)
                current_step += 1
            else:
                pixels[i, j] = modify_pixel(pixels[i, j], (byte & 2) >> 1, byte & 1)
                current_step = 0
                byte_number += 1
                if byte_number >= len(string):
                    return image

    return image


def decrypt_image(path):
    image = Image.open(path)
    size = image.size
    pixels = image.load()

    encoded_len, pos = decrypt(pixels, size, 4)
    length = struct.unpack("I", encoded_len)[0]

    encoded_str, _ = decrypt(pixels, size, length, pos)
    return encoded_str.decode('utf-8')


def decrypt(pixels, size, length, pos=(0, 0)):
    current_step = 0
    res = bytearray()
    byte = 0
    i, j = 0, 0
    for i, j in get_all_indexes(size, pos):
        if len(res) >= length:
            break
        if current_step == 0:
            byte = byte | ((pixels[i, j][0] & 1) << 7) | ((pixels[i, j][1] & 1) << 6) | ((pixels[i, j][2] & 1) << 5)
            current_step += 1
        elif current_step == 1:
            byte = byte | ((pixels[i, j][0] & 1) << 4) | ((pixels[i, j][1] & 1) << 3) | ((pixels[i, j][2] & 1) << 2)
            current_step += 1
        else:
            byte = byte | ((pixels[i, j][0] & 1) << 1) | (pixels[i, j][1] & 1)
            current_step = 0
            res.append(byte)
            byte = 0
    return res, (i, j)


def get_all_indexes(size, pos):
    for j in range(pos[1], size[1]):
        yield pos[0], j

    for i in range(pos[0] + 1, size[0]):
        for j in range(size[1]):
            yield i, j


def modify_pixel(pixel, red, green, blue=None):
    return pixel[0] & 254 | red, pixel[1] & 254 | green, pixel[2] & 254 | blue if blue is not None else pixel[2]
