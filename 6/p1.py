import time

import numpy as np
from pandas import DataFrame

INPUT_FILE = 'input.txt'
GUARD = '^'
OBSTACLE = '#'
EMPTY = '.'
VISITED = 'X'

class RDataFrame(DataFrame):
    def rotate(self, angle = 90):
        if angle == 90:
            temp_df = self.T.reset_index()
            temp_df = temp_df[temp_df.columns[:0:-1]]
            temp_df.columns = range(temp_df.columns.size)
            return RDataFrame(temp_df)
        elif angle == 270:
            return self.rotate().rotate().rotate()
        else:
            raise NotImplementedError('Nuh Uh')

def where_guard(df: DataFrame):
    indices = np.where(df == GUARD)
    row_indices, col_indices = indices[0], indices[1]
    return int(row_indices[0]), int(col_indices[0])

def calculate_guard(df: RDataFrame):
    while True:
        row, col = where_guard(df)
        s = df[col][:row]

        obj_idx = s.where(s == OBSTACLE).last_valid_index()
        if obj_idx is None:
            for i in range(row, -1, -1):
                df.at[i, col] = VISITED
            return (df==VISITED).sum().sum()

        for i in range(row, obj_idx, -1):
            df.at[i, col] = VISITED
        df.at[row, col] = VISITED
        df.at[obj_idx + 1, col] = GUARD
        df = df.rotate(270)

def main():
    data = []

    with open(INPUT_FILE, 'r') as f:
        for line in f:
            data.append(list(line.strip()))

    df = RDataFrame(data)
    print(calculate_guard(df))

if __name__ == '__main__':
    main()