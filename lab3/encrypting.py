from PIL import Image


def encrypt(string, path):
    image = Image.open(path)
    size = image.size
    mode = image.mode

    img_bytes = image.tobytes()
    img_bytes = bytearray(img_bytes)
    if len(string) > len(img_bytes) // 3:
        print("Слишком длинная строка для данного изображения")
        raise OverflowError("Слишком длинная строка для данного изображения")

    i = 0
    for symbol in string:
        symbol = ord(symbol)
        for j in range(8):
            img_bytes[i] = img_bytes[i] // 2 * 2 + symbol % 2
            symbol //= 2
            i += 1
        i += 1

    return Image.frombytes(mode, size, bytes(img_bytes))


def decrypt(path):
    image = Image.open(path)

    img_bytes = image.tobytes()
    img_bytes = bytearray(img_bytes)

    res = bytearray()
    i = 0
    res_byte = 0
    for byte in img_bytes:
        if i == 8:
            i = 0
            if 0 <= res_byte < 128:
                res.append(res_byte)
            res_byte = 0
        else:
            res_byte += byte % 2 * 2 ** i
            i += 1

    return res.decode('ascii')
