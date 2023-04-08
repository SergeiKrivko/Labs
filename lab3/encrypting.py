from PIL import Image
import struct


def encrypt_old(string: str, path):
    image = Image.open(path)
    size = image.size
    mode = image.mode
    img_bytes = image.tobytes()
    del image
    img_bytes = bytearray(img_bytes)

    if len(string) > len(img_bytes) // 9:
        raise OverflowError("too long string for this image")

    string = string.encode('utf-8')
    string = struct.pack("Q", len(string)) + string

    i = 0
    for symbol in string:
        for j in range(8):
            img_bytes[i] = (img_bytes[i] & 254) | symbol % 2
            symbol //= 2
            i += 1
        i += 1

    return Image.frombytes(mode, size, bytes(img_bytes))


def decrypt_old(path):
    image = Image.open(path)

    img_bytes = image.tobytes()

    res = bytearray()
    res_byte = 0
    for i in range(72):
        byte = img_bytes[i]
        if i % 9 == 8:
            res.append(res_byte)
            res_byte = 0
        else:
            res_byte |= (byte & 1) << (i % 9)

    count = struct.unpack("Q", res)[0]

    res.clear()
    res_byte = 0
    for i in range(72, 72 + count * 9):
        byte = img_bytes[i]
        if i % 9 == 8:
            res.append(res_byte)
            res_byte = 0
        else:
            res_byte |= (byte & 1) << (i % 9)

    return res.decode('utf-8')


def encrypt_image(string: str, path):
    image = Image.open(path)
    size = image.size
    if len(string) + 8 > size[0] * size[1] // 3:
        raise OverflowError("too long string for this image")

    pixels = image.load()

    string = string.encode('utf-8')
    string = struct.pack("Q", len(string)) + string

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

    encoded_len, pos = decrypt(pixels, size, 8)
    length = struct.unpack("Q", encoded_len)[0]

    encoded_str, _ = decrypt(pixels, size, length, pos)
    return encoded_str.decode('utf-8')


def decrypt(pixels, size, length, pos=(0, 0)):
    current_step = 0
    res = bytearray()
    byte = 0
    i, j = 0, 0
    for i, j in get_all_indexes(size, pos):
        if len(res) >= length:
            return res, (i, j)
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
