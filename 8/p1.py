from collections import defaultdict
from itertools import pairwise, combinations

INPUT_FILE = 'input.txt'
EMPTY = '.'

def print_board(width, height, nodes, anti_nodes, freq):
    for i in range(height):
        for j in range(width):
            if (i, j) in nodes:
                print(freq((i, j)), end='')
            elif (i, j) in anti_nodes:
                print('#', end='')
            else:
                print('.', end='')
        print()

def main():
    width, height = 0, 0
    data = defaultdict(list)
    with open(INPUT_FILE, 'r') as f:
        x = 0
        for line in f:
            line = list(line.strip())
            for y, elem in enumerate(line):
                if elem == EMPTY:
                    continue
                data[elem].append((x,y))
            width = len(line)
            x += 1
        height = x

    print(width, height)

    anti_nodes = defaultdict(set)
    # print(data)
    for freq, positions in data.items():
        for pos1, pos2 in combinations(positions, 2):
            x_dist = abs(pos1[0] - pos2[0])
            y_dist = abs(pos1[1] - pos2[1])
            if pos1[1] <= pos2[1]:
                anti_nodes[freq].add((pos1[0] - x_dist, pos1[1] - y_dist))
                anti_nodes[freq].add((pos2[0] + x_dist, pos2[1] + y_dist))
            else:
                anti_nodes[freq].add((pos1[0] - x_dist, pos1[1] + y_dist))
                anti_nodes[freq].add((pos2[0] + x_dist, pos2[1] - y_dist))


    for freq, positions in anti_nodes.items():
        anti_nodes[freq] = set([a for a in anti_nodes[freq] if 0 <= a[0] < height and 0 <= a[1] < width])

    all_nodes = {}
    for freq, positions in data.items():
        for p in positions:
            all_nodes[p] = freq

    all_antis = set()
    for freq, positions in anti_nodes.items():
        for p in positions:
            all_antis.add(p)

    print_board(width, height, all_nodes, all_antis, lambda n: all_nodes[n])

    # for freq in data:
    #     print(freq)
    #     print_board(width, height, data[freq], anti_nodes[freq], lambda n: freq)

    print(len(all_antis))




if __name__ == '__main__':
    main()