import numpy as np

if __name__ == '__main__':
    l = [
        [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], 
        [255, 96, 0], [255, 96, 0], [255, 96, 0], [255, 96, 0], [255, 96, 0], [255, 96, 0], [255, 96, 0], [255, 96, 0],
        [187, 255, 0], [187, 255, 0], [187, 255, 0], [187, 255, 0], [187, 255, 0], [187, 255, 0], [187, 255, 0], [187, 255, 0],
        [0, 255, 40], [0, 255, 40], [0, 255, 40], [0, 255, 40], [0, 255, 40], [0, 255, 40], [0, 255, 40], [0, 255, 40],
        [0, 243, 255], [0, 243, 255], [0, 243, 255], [0, 243, 255], [0, 243, 255], [0, 243, 255], [0, 243, 255], [0, 243, 255],
        [0, 17, 255], [0, 17, 255], [0, 17, 255], [0, 17, 255], [0, 17, 255], [0, 17, 255], [0, 17, 255], [0, 17, 255],
        [210, 0, 255], [210, 0, 255], [210, 0, 255], [210, 0, 255], [210, 0, 255], [210, 0, 255], [210, 0, 255], [210, 0, 255],
        [255, 0, 74], [255, 0, 74], [255, 0, 74], [255, 0, 74], [255, 0, 74], [255, 0, 74], [255, 0, 74], [255, 0, 74]
    ]

    nl = np.array(l)
    nl2 = nl.reshape([8, 8, -1])
    print(nl2.reshape([-1, 3]).tolist())

    nl3 = np.rot90(nl2)
    print('\nnp.rot90')
    print(nl3.reshape([-1, 3]).tolist())

    nl4 = np.rot90(nl3)
    print('\nnp.rot90')
    print(nl4.reshape([-1, 3]).tolist())

    nl5 = np.rot90(nl4)
    print('\nnp.rot90')
    print(nl5.reshape([-1, 3]).tolist())

    nl6 = np.rot90(nl5)
    print('\nnp.rot90')
    print((nl6 == nl2).reshape([-1, 3]).tolist())
