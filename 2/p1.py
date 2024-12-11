INPUT_FILE = 'input.txt'

unsafe, total = 0, 0
with open(INPUT_FILE, 'r') as f:
    for line in f:
        total += 1
        data = [int(e) for e in line.split(' ')]
        prev = data[0]
        pos = data[1] > data[0]
        for d in data[1:]:
            if d < prev and pos:
                unsafe += 1
                break
            elif d > prev and not pos:
                unsafe += 1
                break

            if not (1 <= abs(d - prev) <= 3):
                unsafe += 1
                break
            prev = d
print(total - unsafe)