from PIL import Image
import struct


def encrypt(string: str, path):
    image = Image.open(path)
    size = image.size
    mode = image.mode

    img_bytes = image.tobytes()
    img_bytes = bytearray(img_bytes)
    if len(string) > len(img_bytes) // 3:
        raise OverflowError("Слишком длинная строка для данного изображения")

    string = string.encode('utf-8')
    string = struct.pack("Q", len(string)) + string

    i = 0
    for symbol in string:
        for j in range(8):
            img_bytes[i] = (img_bytes[i] >> 1 << 1) + symbol % 2
            symbol //= 2
            i += 1
        i += 1

    return Image.frombytes(mode, size, bytes(img_bytes))


def decrypt(path):
    image = Image.open(path)

    img_bytes = image.tobytes()
    img_bytes = bytearray(img_bytes)

    res = bytearray()
    res_byte = 0
    for i in range(72):
        byte = img_bytes[i]
        if i % 9 == 8:
            res.append(res_byte)
            res_byte = 0
        else:
            res_byte += (byte % 2) << (i % 9)

    count = struct.unpack("Q", res)[0]

    res.clear()
    res_byte = 0
    for i in range(72, 72 + count * 9):
        byte = img_bytes[i]
        if i % 9 == 8:
            res.append(res_byte)
            res_byte = 0
        else:
            res_byte += (byte % 2) << (i % 9)

    return res.decode('utf-8')
