INPUT_FILE = 'input.txt'

def eval_line(data: list[int], can_recurse = False) -> bool:
    prev = data[0]
    pos = data[1] > data[0]
    for d in data[1:]:
        if (d < prev and pos) or \
                (d > prev and not pos) or \
                not (1 <= abs(d - prev) <= 3):
            return (can_recurse and
             any([eval_line(data[:i] + data[i+1:]) for i in range(0, len(data))]))
        prev = d
    return True

def main():
    unsafe, total = 0, 0
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            total += 1
            data = [int(e) for e in line.split(' ')]
            if not eval_line(data, True):
                unsafe += 1

    print(total - unsafe)

if __name__ == '__main__':
    main()