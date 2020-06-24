import pandas as pd


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

    print(df.max())
    print(df['A'].max())
    print(df['A'].sort_values())

    print(df.max(axis=0))
    print(df.max(axis='columns'))

