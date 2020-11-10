
import os
from PIL import Image

file_path = os.path.join(os.path.dirname(__file__), 'data/20120124_ma_8x8fonts_clip.png')

im = Image.open(file_path)
# im.show()

rgb_im = im.convert('RGB')
size = rgb_im.size

rgb_background = (95, 31, 95)
rgb_main_color = (0, 0, 0)
rgb_shadow = (255, 255, 255)

# result = []
# for y in range(size[1]):
#     row = []

#     for x in range(size[0]):
#         # r, g, b = rgb_im.getpixel((x,y))
#         # print(x, y, r,g,b)

#         rgb = rgb_im.getpixel((x,y))

#         if rgb == rgb_background:
#             row.append(0)
#         elif rgb == rgb_main_color:
#             row.append(1)
#         elif rgb == rgb_shadow:
#             row.append(2)
#         else:
#             row.append(-1)

#     result.append(row)

# for i in range(len(result)):
#     print(result[i])


def create_char_pos():
    char_pos = {}

    numerics = ['0', '1', '3', '4', '5', '6', '7', '8', '9']
    for (i, char) in enumerate(numerics):
        char_pos[char] = (i*8, 0) # left, top

    # upper_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # for (i, char) in enumerate(upper_chars):
    #     char_pos[char] = (i*8, 8) # left, top

    # lower_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # for (i, char) in enumerate(lower_chars):
    #     char_pos[char] = (i*8, 16) # left, top

    # symbols = ['.', ',', '-', '+', 'div', '*', '=', '/', '**', '\'', '"', '`', '!', '?', ':', '&', '(', ')', '[', ']', '_', '#', 'deg', 'box']
    # for (i, char) in enumerate(symbols):
    #     char_pos[char] = (i*8, 24) # left, top

    return char_pos
# print(create_char_pos())

char_data = {}

for char, pos in create_char_pos().items():
    char_data[char] = []

    for x in range(pos[0], pos[0]+8):       # 8 dots
        row = []

        for y in range(pos[1], pos[1]+8):   # 8 dots
            rgb = rgb_im.getpixel((x,y))

            if rgb == rgb_background:
                row.append(0)
            elif rgb == rgb_main_color:
                row.append(1)
            elif rgb == rgb_shadow:
                #row.append(2)
                row.append(0)
            else:
                row.append(-1)

        char_data[char].append(row)

import pprint
pprint.pprint(char_data)


def show_char(pos):
    print(pos)
    im = Image.new('RGBA', (8, 8))

    for y in range(8):
        for x in range(8):
            if pos[y][x] == 1:
                im.putpixel((x, y), (255, 255, 255, 0))
            else:
                im.putpixel((x, y), (0, 0, 0,0))

    im.show()


show_char(char_data['0'])
