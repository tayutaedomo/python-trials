import sys
from PIL import Image


RGB_BACKGROUND = (95, 31, 95)
RGB_MAIN_COLOR = (255, 255, 255)
RGB_SHADOW = (0, 0, 0)


class DotCharConverter:
    def __init__(self, file_path):
        self.image = Image.open(file_path).convert('RGB')
        self.char_positions = CharPos8x8.generate()

    def convert_char(self, char):
        pos = self.char_positions.get(char)

        if not pos:
            return None

        left = pos[0]
        top = pos[1]
        width = pos[2]
        height = pos[3]

        converted = []

        for y in range(top, top + height):
            row = []

            for x in range(left, left + width):
                rgb = self.image.getpixel((x, y))
                #print(y, x, rgb)

                if rgb == RGB_BACKGROUND:
                    row.append(0)
                elif rgb == RGB_MAIN_COLOR:
                    row.append(1)
                elif rgb == RGB_SHADOW:
                    row.append(2)
                else:
                    row.append(-1)

            converted.append(row)

        return converted

    def convert_all(self):
        conv_all = {}

        for char in CharPos8x8.NUMERICS:
            conv_all[char] = self.convert_char(char)

        for char in CharPos8x8.UPPER_CHARS:
            conv_all[char] = self.convert_char(char)

        for char in CharPos8x8.LOWER_CHARS:
            conv_all[char] = self.convert_char(char)

        for char in CharPos8x8.SYMBOLS:
            conv_all[char] = self.convert_char(char)

        return conv_all


class CharPos8x8:
    NUMERICS = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    UPPER_CHARS = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    LOWER_CHARS = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    SYMBOLS = [
        '.', ',', '-', '+', 'div', '*', '=', '/', '**', '\'', '"', '`', '!',
        '?', ':', '&', '(', ')', '[', ']', '_', '#', 'deg', 'box'
    ]

    @classmethod
    def generate(cls, width=8, height=8):
        char_pos = {}

        for (i, char) in enumerate(cls.NUMERICS):
            char_pos[char] = (i*8, 0, width, height) # left, top

        for (i, char) in enumerate(cls.UPPER_CHARS):
            char_pos[char] = (i*8, 8, width, height) # left, top

        for (i, char) in enumerate(cls.LOWER_CHARS):
            char_pos[char] = (i*8, 16, width, height) # left, top

        for (i, char) in enumerate(cls.SYMBOLS):
            char_pos[char] = (i*8, 24, width, height) # left, top

        return char_pos


class Font4x8Converter:
    def __init__(self, file_path):
        self.image = Image.open(file_path).convert('RGB')
        self.char_pos = CharPos4x8.generate()

    def convert_char(self, char):
        pos = self.char_pos.get(char)

        if not pos:
            return None

        left = pos[0]
        top = pos[1]
        width = pos[2]
        height = pos[3]

        converted = []

        for y in range(top, top + height):
            row = []

            for x in range(left, left + width):
                rgb = self.image.getpixel((x, y))

                if rgb == RGB_BACKGROUND:
                    row.append(0)
                elif rgb == RGB_MAIN_COLOR:
                    row.append(1)
                elif rgb == RGB_SHADOW:
                    row.append(2)
                else:
                    row.append(-1)

            converted.append(row)

        return converted

    def convert_all(self):
        conv_all = {}

        for char in CharPos4x8.NUMERICS:
            conv_all[char] = self.convert_char(char)

        for char in CharPos4x8.UPPER_CHARS:
            conv_all[char] = self.convert_char(char)

        for char in CharPos4x8.SMALL_NUMERICS:
            conv_all[char] = self.convert_char(char)

        for char in CharPos4x8.LOWER_CHARS:
            conv_all[char] = self.convert_char(char)

        for char in CharPos4x8.SYMBOLS:
            conv_all[char] = self.convert_char(char)

        return conv_all


class CharPos4x8:
    NUMERICS = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    SMALL_NUMERICS = [
        '0s', '1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s'
    ]
    UPPER_CHARS = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    LOWER_CHARS = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    SYMBOLS = [
        '.', ',', '-', '+', 'div', '*', '=', '/', '\'', '"', '!',
        '?', ':', 'deg', '_', 'box', '(', ')', '[2', ']2', '[', ']'
    ]

    @classmethod
    def generate(cls, width=4, height=8):
        char_pos = {}

        for (i, char) in enumerate(cls.NUMERICS):
            char_pos[char] = (i*4, 0, width, height) # left, top

        left = len(cls.NUMERICS) * 4
        for (i, char) in enumerate(cls.UPPER_CHARS):
            char_pos[char] = (left + i*4, 0, width, height) # left, top

        for (i, char) in enumerate(cls.SMALL_NUMERICS):
            char_pos[char] = (i*4, 8, width, height) # left, top

        left = len(cls.SMALL_NUMERICS) * 4
        for (i, char) in enumerate(cls.LOWER_CHARS):
            char_pos[char] = (left + i*4, 8, width, height) # left, top

        for (i, char) in enumerate(cls.SYMBOLS):
            char_pos[char] = (i*4, 16, width, height) # left, top

        return char_pos


def print_char_pos(pos):
    for y in range(len(pos)):
        row = ''
        for x in range(len(pos[0])):
            if pos[y][x] == 1:
                row += '■'
            else:
                row += ' '
        print(row)



if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

        # converted = convert_dot_char_image(file_path)
        # [print(converted[i]) for i in range(len(converted))]

        # converter = DotCharConverter(file_path)
        # print_char_pos(converter.convert_char('0'))
        # for char in CharPos8x8.NUMERICS:
        # for char in CharPos8x8.UPPER_CHARS:
        # for char in CharPos8x8.LOWER_CHARS:
        # for char in CharPos8x8.SYMBOLS:
        #     print_char_pos(converter.convert_char(char))

        converter = Font4x8Converter(file_path)
        print_char_pos(converter.convert_char('A'))
        # for char in CharPos4x8.NUMERICS:
        # for char in CharPos4x8.SMALL_NUMERICS:
        # for char in CharPos4x8.UPPER_CHARS:
        # for char in CharPos4x8.LOWER_CHARS:
        # for char in CharPos4x8.SYMBOLS:
            # print_char_pos(converter.convert_char(char))

    else:
        #print(CharPos8x8.generate())
        print(CharPos4x8.generate())
