INPUT_FILE = 'input.txt'

lst0, lst1 = [], []

with open(INPUT_FILE, 'r') as f:
    for line in f:
        e0, e1 = line.split('   ')
        lst0.append(int(e0))
        lst1.append(int(e1))

sorted_lst0 = sorted(lst0)
sorted_lst1 = sorted(lst1)
print(sum([abs(e - sorted_lst1[i]) for i, e in enumerate(sorted_lst0)]))