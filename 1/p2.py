import pandas as pd

INPUT_FILE = 'input.txt'

lst0, lst1 = [], []

with open(INPUT_FILE, 'r') as f:
    for line in f:
        e0, e1 = line.split('   ')
        lst0.append(int(e0))
        lst1.append(int(e1))

pd1 = pd.Series(lst1).value_counts()
print(sum([e * (pd1[e] if e in pd1 else 0) for e in lst0]))