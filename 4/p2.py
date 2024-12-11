import re

from pandas import DataFrame

INPUT_FILE = 'input.txt'
FIND_STR = r'MAS'

class RDataFrame(DataFrame):
    def rotate(self, angle = 90):
        if angle == 90:
            temp_df = self.T.reset_index()
            return temp_df[temp_df.columns[:0:-1]]
        elif angle == 180:
            return RDataFrame(self.rotate()).rotate()
        elif angle == 270:
            return RDataFrame(RDataFrame(self.rotate()).rotate()).rotate()
        else:
            raise NotImplementedError('Nuh Uh')

def find_x_mas(df: DataFrame) -> int:
    found = 0
    temp_df = df.reset_index()
    temp_df = temp_df[temp_df.columns[1:]]
    temp_df.columns = range(temp_df.columns.size)
    for i in range(temp_df.shape[0]):
        for j in range(temp_df.shape[1]):
            try:
                if all([temp_df[j + k][i + k] == l for k, l in enumerate(FIND_STR)] +
                       [temp_df[j + k][i + (2-k)] == l for k, l in enumerate(FIND_STR)]):
                    found += 1
            except KeyError:
                pass
    print('diag:', found)
    return found

def main():
    found = 0
    with open(INPUT_FILE, 'r') as f:
        data = []
        for line in f:
            data.append(list(line.strip()))
        df = RDataFrame(data)
        for round, c_df in enumerate([df, df.rotate(), df.rotate(180), df.rotate(270)]):
            print(round)
            found += find_x_mas(c_df)

    print(found)

if __name__ == '__main__':
    main()