from PIL import Image


def mirror_image(path, new_path):
    image = Image.open(path)
    n, m = image.size

    pixels = image.load()

    for i in range(n // 2):
        for j in range(m):
            pixels[i, j], pixels[n - 1 - i, m - 1 - j] = pixels[n - 1 - i, m - 1 - j], pixels[i, j]
    if n % 2:
        i = n // 2 + 1
        for j in range(m // 2):
            pixels[i, j], pixels[n - 1 - i, m - 1 - j] = pixels[n - 1 - i, m - 1 - j], pixels[i, j]

    image.save(new_path)
