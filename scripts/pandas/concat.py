import pandas as pd


if __name__ == '__main__':
    # Reference: https://deepage.net/features/pandas-concat.html

    df1 = pd.DataFrame(
        {
            'A': ['A0', 'A1', 'A2', 'A3'],
            'B': ['B0', 'B1', 'B2', 'B3']
        },
        index=[0, 1, 2, 3]
    )

    print(df1)

    df2 = pd.DataFrame(
        {
            'A': ['A4', 'A5', 'A6'],
            'C': ['C4', 'C5', 'C6']
        },
        index= [4, 5, 6]
    )

    print(df2)

    print('pd.concat([df1, df2])')
    print(pd.concat([df1, df2]))

    df3 = pd.DataFrame(
        {
            'A': ['A4'],
            'B': ['B4']
        }
    )

    print('pd.concat([df1, df3])')
    print(pd.concat([df1, df3]))

    print('pd.concat([df1, df3], ignore_index=True)')
    print(pd.concat([df1, df3], ignore_index=True))

    print('pd.concat([df3, df1], ignore_index=True)')
    print(pd.concat([df3, df1], ignore_index=True))

