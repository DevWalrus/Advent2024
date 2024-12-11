import re
from collections import deque

INPUT_FILE = 'input.txt'

def bfs(data: list[list[int]], start: tuple[int, int]):
    queue: deque[list[tuple[int, int]]] = deque()
    found = 0

    path = [start]
    queue.append(path.copy())
    while queue:
        path = queue.popleft()
        # print(path)
        current = path[-1]

        if data[current[0]][current[1]] == 9:
            found += 1

        for neighbor in [
            (current[0] - 1, current[1]),
            (current[0] + 1, current[1]),
            (current[0], current[1] - 1),
            (current[0], current[1] + 1)]:

            if 0 <= neighbor[0] < len(data) and 0 <= neighbor[1] < len(data[0]):
                if neighbor not in path and data[neighbor[0]][neighbor[1]] == data[current[0]][current[1]] + 1:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    queue.append(new_path)

    return found

def main():
    data = []
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            data.append([int(n) for n in list(line.strip())])

    starts = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 0:
                starts.append((i, j))

    print(sum([bfs(data, s) for s in starts]))



if __name__ == '__main__':
    main()