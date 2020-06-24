import pandas as pd
import numpy as np


if __name__ == '__main__':
    # Reference: https://deepage.net/features/pandas-max-min.html

    df = pd.DataFrame({
        "A": [1, -1, 0, 9, 8, 1, -10],
        "B": [-1, 0, 7, 6, 1, 3, 2],
        "C": ['A', 'B', 'c', 'D', 'C', 'a', 'b']
    })

    print(df)
    print(df.describe())
    print(df['A'].describe())

    print('')
    print('Max')
    print(df.max())
    print(df['A'].max())
    print(df['A'].sort_values())

    print('')
    print('Max:axis')
    print(df.max(axis=0))
    print(df.max(axis='columns'))

    print('')
    print('Max:skipna')
    df.iloc[3, 0] = np.nan
    df.iloc[3, 2] = np.nan
    print(df)
    print(df.max())
    print(df.max(skipna=False))

    print('')
    print('Max:numeric_only')
    df['C'] = df['C'].fillna("missing")
    print(df)
    print(df.max(numeric_only=True))
    print(df.max(numeric_only=False))


    df = pd.DataFrame({
        "A": [1, -1, 0, 9, 8, 1, -10],
        "B": [-1, 0, 7, 6, 1, 3, 2],
        "C": ['A', 'B', 'c', 'D', 'C', 'a', 'b']
    })

    print(df)

    print('')
    print('Min')
    print(df.min())
    print(df['B'].min())
    print(df['B'].sort_values())

