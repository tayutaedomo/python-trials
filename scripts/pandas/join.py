import pandas as pd
import numpy as np


if __name__ == '__main__':
    a = np.array([
        [0.00899, 0.00001, 0.99081, 0.0002],
        [0.00182, 0.00163, 0.97249, 0.02406],
        [1.0, 0.0, 0.0, 0.0],
        [0.99991, 0.00001, 0.00006, 0.00002],
        [0.00239, 0.0305, 0.82374, 0.14337],
    ])
    b = np.array(
        ['3510', '1586', '1186', '3671', '3317']
    )

    dfa = pd.DataFrame(a, columns=[0, 1, 2, 3])
    print(dfa)

    dfb = pd.DataFrame(b, columns=['book_id'])
    print(dfb)

    print(dfa.join(dfb))

