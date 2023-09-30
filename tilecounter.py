from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time


def prep_exit():
    print("Press enter to exit program.")
    input()


def sum_unique(pic):
    unique = Image.new("RGB", pic.size)
    t = time.time()
    x_tiles = pic.size[0] // 8 # the number of tiles horizontally
    y_tiles = pic.size[1] // 8 # the number of tiles vertically
    set_of_unique_tiles = set()
    print("Total tiles: " + str(x_tiles * y_tiles))
    for rise in range(0, y_tiles):
        for run in range(0, x_tiles):
            tile = []
            for y in range(0 + 8 * rise, 8 + 8 * rise):
                for x in range(0 + 8 * run, 8 + 8 * run):
                    pixel = pic.getpixel((x, y))
                    for i in range(0, 3):
                        tile.append(chr(pixel[i]))
                    # tile.append(pixel) // first idea - I think checking a single int instead of a tuple is 4x faster.
            tile = ''.join(tile)
            if not(tile in set_of_unique_tiles):
                set_of_unique_tiles.update({tile})
                for y in range(0 + 8 * rise, 8 + 8 * rise):
                    for x in range(0 + 8 * run, 8 + 8 * run):
                        unique.putpixel((x, y), (255, 255, 255))

    print("Elapsed time: " + str(time.time() - t))
    print("Unique Tiles: " + str(len(set_of_unique_tiles)))
    print("Every white space in this image represents the first instance of a unique tile.")
    unique.show()
    prep_exit()


if __name__ == '__main__':
    path = askopenfilename()
    image = Image.open(path)
    if image.size[0] % 8 != 0 and image.size[1] % 8 != 0:
        print("Image width and height must both be divisible by 8")
        prep_exit()
        exit()
    sum_unique(image)
