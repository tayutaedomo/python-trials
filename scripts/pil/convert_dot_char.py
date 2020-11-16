import os
import sys
import json

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(os.path.abspath(ROOT_PATH))

from scripts.pil.dot_char import DotCharConverter


if __name__ == '__main__':
    file_path = sys.argv[1]
    converter = DotCharConverter(file_path)

    conv_all = converter.convert_all()
    # print(conv_all)

    dest_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'dot_char.json')
    with open(dest_path, 'w') as f:
        json.dump(conv_all, f)

    print('Exported successfully.', dest_path)